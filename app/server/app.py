from fastapi import FastAPI, HTTPException
from fastapi_mqtt import FastMQTT, MQTTConfig
from typing import Optional, Text, List, Dict
import json
from datetime import datetime
import uvicorn
from uuid import uuid4 as uuid
from bson import ObjectId
from server.routes.rackroutes import router as RackRouter
from server.mqtt.mqttconfig import mqtt


app = FastAPI()                                   # fast api app
mqtt.init_app(app)                                # init mqtt service in fastapi
app.include_router(RackRouter)



