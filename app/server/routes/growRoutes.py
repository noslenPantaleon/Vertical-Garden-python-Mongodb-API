from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from server.mqtt.mqttfuntions import growRoom_data
from server.mqtt.mqttconfig import mqtt
from server.automation.automation_control import(
    automation_lights,
    automation_coolers,
    automation_waterpumps)
from server.automation.automation_cycle import(
    send_mqtt_message_automation,
    )
from server.models.growRoomModel import(
    Growroom,
    GrowroomUpdate,
    Growcycle,)
from server.models.automationModel import(
    AutomationSwicht,
    AutomationTimer,
    MqttMessage,)
from server.database import (
    get_growroom_id,
    get_all_growrooms,
    get_growroom_sensors_id,
    add_new_growroom,
    get_all_sensor_data,
    update_growroom_items,
    get_growroom_name_sensor_data,
    delete_growroom,
    save_automation,
    delete_sensor_data,
    )

router = APIRouter()
growlist =[]


# get the sensor data by growroom id
@router.post('/creategrowroom', response_model=Growroom)
async def create_growroom(growroom: Growroom):
    data = dict(growroom)
    response = await add_new_growroom(data)
    if response:
        return response
    raise HTTPException(400, "Bad Request")

# send mqtt message to an specific growroom and topic
@router.post("/sendmessage")
async def send_mqtt_message(mqttMessage: MqttMessage):
    mqttData = mqttMessage.mqtt_message                      # mqtt message
    topic = mqttMessage.mqtt_subtopic                        # use rack name as a subtopic
    mqtt.publish(f"{topic}", f"{mqttData}")                  # publishing mqtt topic
    return {"result": mqttData}


# imput growroom id as a parameter and get growroom data created by id
@router.get('/growroom/{Growroom_id}', response_model=Growroom)
async def get_Growroom(Growroom_id):
    response = await get_growroom_id(Growroom_id)
    if response:
        return response
    raise HTTPException(404, f"Item not found {Growroom_id}")

# get a list with all the the created growrooms
@router.get('/growroomlist')
async def get_Growroom_List():
    response = await get_all_growrooms()
    if response:
        return response
    raise HTTPException(status_code=404, detail="Item not found")


# get a list with all the the created growrooms
@router.get('/growroomssensordata')
async def get_Growroom_sensor_data_List():
    response = await get_all_sensor_data()
    if response:
        return response
    raise HTTPException(status_code=404, detail="Item not found")


# imput growroom sensor data by id 
@router.get('/growroomsensorid/{sensor_id}')
async def get_Growroom_sensor_id(sensor_id):
    response = await get_growroom_sensors_id(sensor_id)
    if response:
        return response
    raise HTTPException(404, f"Item not found {sensor_id}")

# get the sensor data by growroom name 
# @router.get("/sensordata/{Growroom_name}", )
# async def get_growroom_sensordata(Growroom_name):
#     response = await get_growroom_name_sensor_data (Growroom_name)
#     if response:
#         return response
#     raise HTTPException(404, f"Item not found {Growroom_name}")
  
# update growroom by id
@router.put('/updategrowroom/{Growroom_id}', response_model=GrowroomUpdate)
async def update_rack(Growroom_id: str,  model: GrowroomUpdate):
    data = dict(model)
    response = await update_growroom_items(Growroom_id, data)
    if response:
        return response 
        
    raise HTTPException(status_code=404, detail="Item not updated")

# add a realtime swicht_ on/off by growroom id
@router.put('/automationswicht/{Growroom_id}', response_model= AutomationSwicht)
async def rack_automation_swicht_on_off(Growroom_id: str, model: AutomationSwicht):
    data = dict(model)
    funtion_automation_lights = automation_lights(data)
    # funtion_automation_coolers = automation_coolers(data)
    funtion_automation_waterpumps =  automation_waterpumps(data)
    response = await save_automation(Growroom_id, data)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Item not saved")

# add an automation cycle file by growroom id 
@router.put('/saveautomationcycle/{Growroom_id}', response_model= AutomationTimer)
async def save_automation_cycle(Growroom_id: str, model:  AutomationTimer):
    data = dict(model)
    automation = send_mqtt_message_automation(Growroom_id, data)
    response = await save_automation(Growroom_id, data)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Item not saved")

# delete growroom by id
@router.delete('/deletegrowroom/{Growroom_id}')
async def remove_growroom(Growroom_id: str):
    response = await delete_growroom(Growroom_id)
    if response:
        return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# delete sensordata by id
@router.delete('/deletesensordata/{object_id}')
async def delete_sensors_data(object_id: str):
    response = await delete_sensor_data(object_id)
    if response:
        return {"message": "Post has been deleted succesfully"}
    raise HTTPException(status_code=404, detail="Item not found")

