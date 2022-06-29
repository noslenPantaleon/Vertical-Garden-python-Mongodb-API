from server.models.automationModel import(
    AutomationSwicht,
    AutomationTimer,
    MqttMessage,)
from server.models.growRoomModel import(
    Growroom,
    GrowroomUpdate,
                )
from datetime import datetime
from server.mqtt.mqttconfig import mqtt
import json

datetime_now = datetime.now()
print(datetime_now.strftime('%d/%m/%Y %H:%M:%S'))
hour = (datetime_now.strftime('%H'))

def send_mqtt_message_automation(Growroom_id, model):
    topic= "automations"                       
    mqtt.publish(f"{topic}", f"{Growroom_id }") 
   

    








