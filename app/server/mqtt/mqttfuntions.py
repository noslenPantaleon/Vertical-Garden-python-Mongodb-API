from server.mqtt.mqttconfig import mqtt
from datetime import datetime
from server.database import save_sensor_data
import time
import json

datetime_now = datetime.now()
hour= (datetime_now.strftime ('%H'))
minutes= (datetime_now.strftime ('%M'))
seconds= (datetime_now.strftime ('%S')) 

growRoom_data = {}
topic= "growroom01"

# susbcribe to the topic on conecct to the mqtt broker
@mqtt.on_connect()
def on_connect(client, flags, rc, properties):
    client.subscribe(topic)  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

# recieve mqtt message
@mqtt.on_message()
async def mqtt_message(client, topic, payload, qos, properties):
    
    global growRoom_data

    # decode json data from payload
    mqtt_decode = str(payload.decode("utf-8", "ignore"))
    # convert into python dictionary
    growRoom_data = json.loads(mqtt_decode)
    growRoom_data["time"] = datetime_now

    print("Received message: ", topic, payload.decode(), qos, properties)
    # calling funtion to save data in database
    save_Data = await save_sensor_data (growRoom_data)      
    return growRoom_data 


# mqtt disconnect info
@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

# mqtt subscribe info
@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)






