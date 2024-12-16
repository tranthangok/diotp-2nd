The Diotp Project - The humidity task
------------------------------------------------------
http://135.236.208.169

*IMPORTANT: Currently it's not avaiable to see the data in frontend part, you can ask me to show username and pass in INFLUXDBINFLUXDB* 

Overall Instruction:
The project through out the process of collecting the data with using embedded devices, transmitting, analyzing in Backend part and showing the data in the Frontend part. It can used and updated in real-time operation to show the humidity rate around the area with the sensor based on the embedded devices. After that, it will transfer through api to update to the Frontend part with a chart to show the humidity rate.
All the softwares have been used in this project and how it cost:
- Embedded device: Raspberry Pi Pico with humidity sensor based on - Can be lended from the uni (Cost around 30-50 Euros) 
- Cloud Service - VPS: Azure VM running on Ubuntu - 0.017 Euros/hour with student subscription
- Web service: Nginx 1.24 - Free
- Frontend part: Using HTML file with CSS and JavaScript customization - Free
- Backend part: NodeJS 23.0, InfluxDB to save and show DB - Free

How to use on the web link:
- http://135.236.208.169: Displays the chart and shows real-time operation
- http://135.236.208.169/api/v1/embed?value=...: Input the interger and memorize it on the DB
- http://135.236.208.169/api/v1/get-data: Showing the data has been saved in the past

How it works? And their benefits:

Fron the embedded device: Codding a program and connecting to the device by the cable: 
- First, it gathers the surrounding data through sensor DHT11-GP0
- Beside, it is connecting to the WiFi through SSID and password
- And after that it sends the data to the backend from a HTTP request
- Repeat the process again until the user disconnected the device or has error

In Azure Cloud Service:
- All the Frontend and Backend operates on VPS 24/7
- Azure Service handles good storage scaling and performance for the parts

With web service (Nginx):
- Optimize for handling many requests, serve static Frontend content directly to users
- It is a bridge between Frontend and Backend part
- Increases response time and support multiples types of streaming
- Secures the web communications and requests, encrypts traffic and limits the attacks

Backend process:
- It takes the value from the request in embedded device through the api-link 
- After that it transfers the raw data and makes sure that it is a proper number to the next step
- It saves and shows on the InfluxDB and creates the timestamp on that.
- Finally, retrieves the data and fetching the data from the InfluxDB in several days before.

Lastly, Frontend process:
- Taking the analyzed data from the DB 
- Real-time view for the users
