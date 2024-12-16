import time
import machine
import network
import urequests as requests

SSID = "wifi"
PASSWORD = "password"
API_ENDPOINT = "http://135.236.208.169/api/v1/embed"

INTERVAL = 3
DHT_PIN = machine.Pin(0)

try:
    from dht import DHT11 
    sensor = DHT11(DHT_PIN)
except ImportError:
    print("DHT library not found. Please ensure MicroPython firmware supports the 'dht' module.")
    raise

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > 10:  
                print("Failed to connect to WiFi")
                return False
            time.sleep(0.5)
    print("WiFi connected!")
    return True

if not connect_to_wifi():
    print("Cannot connect to WiFi. Exiting program.")
    while True:
        time.sleep(1)

while True:
    try:
        sensor.measure()
        humidity = sensor.humidity() 
        print(f"Humidity: {humidity:.1f}%")

        response = requests.get(f"{API_ENDPOINT}?value={humidity}")
        print(f"Server response: {response.status_code}, {response.text}")
        response.close()
    except OSError as e:
        print("Sensor error:", e)

    time.sleep(INTERVAL)