from server.models.rackautomationmodel import(
    RackAutomationSwicht,
    RackAutomationTimer,
    MqttMessage,)
from server.models.rackmodel import(
    Rack,
    RackUpdate,
                )
from datetime import datetime
from server.mqtt.mqttconfig import mqtt
import json

datetime_now = datetime.now()
print(datetime_now.strftime('%d/%m/%Y %H:%M:%S'))
hour = (datetime_now.strftime('%H'))

def daylight_cycle(model):

    global hour
    now_hour= int(hour)
    data = model
    rackSubTopic= data["rack_name"]                       
    mqtt.publish(f"microstation/{rackSubTopic}", f"{data }") 
   

    








"""

    coolers_on = data["coolers_on"]
    coolers_off = data["coolers_off"] 
    waterpumps_on = data["waterpumps_on"]
    waterpumps_off = data["waterpumps_off"]


    # for  key  in automation.keys():
    #      val = automation[key]
    #      lights= val.get("lights")
    #      print (lights)
    #      return automation
    # dato1 = (([key for key in automation.keys()][0], [
    #          value for value in automation.values()][0]))
    # return {"result": dato1}


# diccionario a analizar
# rack = {
#     "lights": {
#         "light1": True,
#         "light2": True,
#         "light3": False,
#         "light4": False
#     },

#     "coolers": {
#         "coolers1": True,
#         "coolers2": True,
#         "coolers3": True,
#         "coolers4": True
#     },
#     "waterpumps": {
#         "waterpumps1": True,
#         "waterpumps2": False,
#     }
# }
"""