import motor.motor_asyncio
from server.models.growRoomModel import Growroom, GrowroomUpdate, Growcycle
from server.models.automationModel import AutomationTimer, AutomationSwicht
from bson import ObjectId
from datetime import datetime
import json
from bson import json_util

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')  # mongodb uri
db = client.microstation                             # mongodb database
collection = db.growroom                            # mongodb collection
collection_sensors = db.growroom_sensors	        # mongodb collection
datetime_now = datetime.now()

# fetch growroom by id in database
async def get_growroom_id(Growroom_id):
    document = await collection.find_one({"_id": ObjectId(Growroom_id)})  
    return document

# fetch all growroom by id in database
async def get_all_growrooms():                                        
    Growroom_id = []
    cursor = collection.find({})
    async for document in cursor:
        Growroom_id.append(Growroom(**document))
    return Growroom_id

# fetch sensor data growroom by id in database
async def get_growroom_sensors_id(sensor_id):
    document = await collection_sensors.find_one({"_id": ObjectId(sensor_id)})  
    return document

# fetch all sensor data of growrooms by id in database
async def get_all_sensor_data():                                        
    data=[]
    cursor = collection_sensors.find({})
    async for document in cursor:
        sensors=document
        growRoom_data = json.loads(json_util.dumps(sensors))
        data.append(growRoom_data)
        return {"json":growRoom_data}

# save new growroom in database                                                   
async def add_new_growroom(data_rack):
    document = data_rack
    result = await collection.insert_one(document)
    return document

# update growroom items in database                                        
async def update_growroom_items(Growroom_id,  model):
    document = await collection.find_one({"_id": ObjectId(Growroom_id)})  
    await collection.update_one({"_id": ObjectId(Growroom_id)}, {"$set": model})
    saveDocument = await collection.find_one({"_id": ObjectId(Growroom_id)})
    return document

# remove growroom in database                                              
async def delete_growroom(Growroom_id):
    await collection.delete_one({"_id": ObjectId(Growroom_id)})
    return True

# remove growroom sensor data in database                                              
async def delete_sensor_data(object_id):
    await collection_sensors.delete_one({"_id": ObjectId(object_id)})
    return True

# save sensor data by growroom id in database                                
async def save_sensor_data(data):
   
    result = await collection_sensors.insert_one(data)
    return result

# save sensor data by growroom id in database                                
async def get_growroom_name_sensor_data(data): 
    result = await collection_sensors.find({"growroom_name" :data})
    return result




 




# add automations by grow id
async def save_automation(Growroom_id, model):
    automation = model
    document = await collection.find_one({"_id": ObjectId(Growroom_id)})
    await collection.update_one({"_id": ObjectId(Growroom_id)}, {"$set": model})
    return document



  