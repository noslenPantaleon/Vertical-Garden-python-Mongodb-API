from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.mqtt.mqttfuntions import rack_data
from server.mqtt.mqttconfig import mqtt
from server.automation.automation_control import(
    automation_lights,
    automation_coolers,
    automation_waterpumps,)
from server.automation.automation_cycle import(
    daylight_cycle,
    )
from server.models.rackmodel import(
    Rack,
    RackUpdate,
    Growcycle,)
from server.models.rackautomationmodel import(
    RackAutomationSwicht,
    RackAutomationTimer,
    MqttMessage,)
from server.database import (
    get_rack_id,
    get_all_racks_id,
    add_new_rack,
    update_rack_items,
    delete_rack,
    save_automation,
    save_sensor_data,
    delete_sensor_data,
    )

router = APIRouter()
rack_list = []
growlist = []


# imput rack id as a parameter and get data rack created by id
@router.get('/rack/{rack}', response_model=Rack)
async def get_rack(rack):
    response = await get_rack_id(rack)
    if response:
        return response
    raise HTTPException(404, f"Item not found {rack}")

# get a list with all the the created racks
@router.get("/racklist")
async def get_rackList():
    response = await get_all_racks_id()
    return response

# get the sensor data by rack id (Not finish yet)
@router.get("/sensordata")
async def get_sensordata():
    return rack_data

# get the growlist
@router.get("/growcyclelist")
async def grow_plants_list():
    return growlist

# get the sensor data by rack id
@router.post('/createrack', response_model=Rack)
async def create_rack(rack: Rack):
    data = dict(rack)
    response = await add_new_rack(data)
    if response:
        return response
    raise HTTPException(400, "Bad Request")

# send mqtt message to an specific rack and topic
@router.post("/sendmessage")
async def send_mqtt_message(mqttMessage: MqttMessage):
    mqttData = mqttMessage.mqtt_message                         # mqtt message
    subtopic = mqttMessage.mqtt_subtopic                        # use rack name as a subtopic
    mqtt.publish(f"microstation/{subtopic}", f"{mqttData}")     # publishing mqtt topic
    return {"result": mqttData}

# create growcycle with plants characteristics
@router.post("/creategrowcycle")
async def growcycle(growcycle: Growcycle):
    growing = dict(growcycle)
    growlist.append(growing)
    return {"result": growcycle}

# add an automation by rackid by analysing json message
@router.put('/automationswicht/{rack_id}', response_model= Rack)
async def rack_automation_swicht_on_off(rack_id: str, model:  Rack):
    data = dict(model)
    funtion_automation_lights = automation_lights(data)
    # funtion_automation_coolers = automation_coolers(data)
    funtion_automation_waterpumps =  automation_waterpumps(data)
    response = await save_automation(rack_id, data)

# add an automation by rackid 
@router.put('/automationtioncycle/{rack_id}', response_model= RackAutomationTimer)
async def rack_automation_cycle(rack_id: str, model:  RackAutomationTimer):
    data = dict(model)
    rackSubTopic = model.rack_name  
    automation = daylight_cycle(data)
    response = await save_automation(rack_id, data)
    
# update rack by id
@router.put('/update/{rack_id}', response_model=RackUpdate)
async def update_rack(rack_id: str,  model: RackUpdate):
    data = dict(model)
    response = await update_rack_items(rack_id, data)
    if response:
        return response
    raise HTTPException(status_code=404, detail="Item not found")

# delete rack by id
@router.delete('/deleterack/{rack_id}')
async def remove_rack(rack_id: str):
    response = await delete_rack(rack_id)
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



