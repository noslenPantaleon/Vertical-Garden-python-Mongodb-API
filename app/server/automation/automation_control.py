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

datetime_now = datetime.now()
print(datetime_now.strftime('%d/%m/%Y %H:%M:%S'))
hour = (datetime_now.strftime('%H'))

# buscar a traves del key el valor y guardarlo en variables separadas
def automation_lights(model):

    data = model
    subTopic= data["rack_name"]                       
    lights = data["add_lights"]                                      # buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave lights en nuevo diccionario
    light1 = (lights['light1'])                                      # buscamos el valor de la key light1 dentro del diccionario lights
    light2 = (lights['light2'])
    light3 = (lights['light3'])
    light4 = (lights['light4'])

    if light1:
        mqtt.publish(f"microstation/{subTopic}", "light1_on")        # si el valor es True envia mensaje para encender luces
    elif light1 == False:
        mqtt.publish(f"microstation/{subTopic}", "light1_off")        # si el valor es True envia mensaje para encender luces

    if light2:
        mqtt.publish(f"microstation/{subTopic}", "light2_on")        # si el valor es True envia mensaje para encender luces
    elif light2 == False:
        mqtt.publish(f"microstation/{subTopic}", "light2_off")        # si el valor es True envia mensaje para encender luces

    if light3:
        mqtt.publish(f"microstation/{subTopic}", "light3_on")        # si el valor es True envia mensaje para encender luces
    elif light3 == False:
        mqtt.publish(f"microstation/{subTopic}", "light3_off")        # si el valor es True envia mensaje para encender luces

    if light4:
        mqtt.publish(f"microstation/{subTopic}", "light4_on")        # si el valor es True envia mensaje para encender luces
    elif light4 == False:
        mqtt.publish(f"microstation/{subTopic}", "light4_off")        # si el valor es True envia mensaje para encender luces

# buscar a traves del key el valor y guardarlo en variables 
def automation_coolers(model):
    data = model
    subTopic= data["rack_name"]
    coolers = data["add_coolers"]                                    # buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave lights en nuevo diccionario
    coolers1 = (coolers['coolers1'])                                 # buscamos el valor de la key coolers1 dentro del diccionario coolers
    coolers2 = (coolers['coolers2'])
    coolers3 = (coolers['coolers3'])
    coolers4 = (coolers['coolers4'])

    if coolers1:
        mqtt.publish(f"microstation/{subTopic}", "cooler1_on")       # si el valor es True envia mensaje para encender luces
        return light1    
    else:
        mqtt.publish(f"microstation/{subTopic}", "cooler1_off")      # publish
        return light1
    print('-' * 80)

    if coolers2:
        mqtt.publish(f"microstation/{subTopic}", "cooler2_on")       # si el valor es True envia mensaje para encender luces
        return light1    
    else:
       
        mqtt.publish(f"microstation/{subTopic}", "cooler2_off")      # publish
        return light1
    print('-' * 80)

    if coolers3:
        mqtt.publish(f"microstation/{subTopic}", "cooler3_on")       # si el valor es True envia mensaje para encender luces
        return light1    
    else:
       
        mqtt.publish(f"microstation/{subTopic}", "cooler3_off")      # publish
        return light1
    print('-' * 80)

    if coolers4:
        mqtt.publish(f"microstation/{subTopic}", "cooler4_on")       # si el valor es True envia mensaje para encender cooler
        return light1    
    else:
       
        mqtt.publish(f"microstation/{subTopic}", "cooler4_off")      # publish
        return light1
    print('-' * 80)

# buscar a traves del key el valor y guardarlo en variables separadas
def automation_waterpumps(model):

    data = model
    subTopic= data["rack_name"]
    waterpumps = data["add_waterpumps"]                             # buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave waterpumps en nuevo diccionario
    waterpumps1 = (waterpumps['waterpumps1'])                       # buscamos el valor de la key waterpump1 dentro del diccionario waterpumps
    waterpumps2 = (waterpumps['waterpumps2'])

    if waterpumps1:
        mqtt.publish(f"microstation/{subTopic}", "waterpumps1_on")  # publish
        return waterpumps1                                          # si el valor es True envia mensaje para encender bomba1
     
    else:
        mqtt.publish(f"microstation/{subTopic}", "waterpumps1_off")  # publish
        return waterpumps1                                          # si el valor es True envia mensaje para encender bomba1
  
    print('-' * 80)

    if waterpumps2:
        mqtt.publish(f"microstation/{subTopic}", "waterpumps_on")  # publish
        return waterpumps2                                          # si el valor es True envia mensaje para encender bomba1
     
    else:
        mqtt.publish(f"microstation/{subTopic}", "waterpumps_off")  # publish
        return waterpumps2 

    print('-' * 80)


def automation_electrovalvules(model):

    data = model
    subTopic= data["rack_name"]                       
    electrovalvules = data["add_electrovalvules"]                                      # buscamos dentro del diccionario rack y guardamos el diccionario que esta adentro de la clave lights en nuevo diccionario
    electrovalvule1 = (electrovalvules['electrovalvule1'])                                      # buscamos el valor de la key light1 dentro del diccionario lights
    electrovalvule2 = (electrovalvules['electrovalvule1'])
    electrovalvule3 = (electrovalvules['electrovalvule1'])
    electrovalvule4 = (electrovalvules['electrovalvule1'])

    if electrovalvules1:
        mqtt.publish(f"microstation/{subTopic}", "irrigation_1a")        # si el valor es True envia mensaje para encender electrovalvules1
     

    if electrovalvule2:
        mqtt.publish(f"microstation/{subTopic}", "irrigation_1b")        # si el valor es True envia mensaje para encender electrovalvules2
    
    if electrovalvules3:
        mqtt.publish(f"microstation/{subTopic}", "irrigation_2a")        # si el valor es True envia mensaje para encender electrovalvules3
    
    if electrovalvules4:
        mqtt.publish(f"microstation/{subTopic}", "irrigation_2b")        # si el valor es True envia mensaje para encender electrovalvules4
    








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