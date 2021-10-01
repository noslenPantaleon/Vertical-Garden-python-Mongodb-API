from pydantic import BaseModel, ValidationError, conint
from typing import Optional, Text, List, Dict 
from datetime import datetime
from time import time
import uvicorn



# model to send mqtt message 
class MqttMessage (BaseModel):
    mqtt_message: str
    mqtt_subtopic: str


# model to create rack automation
class RackAutomationTimer (BaseModel):
    rack_name: str
    lights_on: Dict[str,  int]
    lights_off: Dict[str, int]
    coolers_on:  Dict[str, int]
    coolers_off:  Dict[str, int]
    waterpumps_on: Dict[str, int]
    waterpumps_off: Dict[str, int]
    electrovalvules_on: Dict[str, bool]
    electrovalvules_off: Dict[str, bool]
    created_at: datetime = datetime.now()


    class Config:
        schema_extra = {
        "example":{
        "rack_name": "comunication",

        "lights_on": {
            "light1": 8,
            "light2": 8,
            "light3": 8,
            "light4": 8
        },

        "lights_off": {
            "light1": 9,
            "light2": 9,
            "light3": 9,
            "light4": 9
        },

        "coolers_on": {
            "coolers1": 8,
            "coolers2": 8,
            "coolers3": 8,
            "coolers4": 8
        },

        "coolers_off": {
            "coolers1": 9,
            "coolers2": 9,
            "coolers3": 9,
            "coolers4": 9
        },

        "waterpumps_on": {
            "waterpumps1": 8,
            "waterpumps2": None
           
        },

        "waterpumps_off": {
            "waterpumps1": 8,
            "waterpumps2": None
          },

        "electrovalvules_on": {

            "electrovalvule1": 8,
            "electrovalvule2": 9,
            "electrovalvule3": 10
            "electrovalvule4": 11

      },

          "electrovalvules_off": {

            "electrovalvule1": 9,
            "electrovalvule2": 10,
            "electrovalvule3": 11
            "electrovalvule4": 12

      },

        }
         }


# model to create rack automation
class RackAutomationSwicht (BaseModel):

    rack_name: str
    add_lights: Dict[str, bool]
    add_coolers:  Dict[str, bool]
    add_waterpumps: Dict[str, bool]
    lights_on: Dict[str,  int]
    lights_off: Dict[str, int]
    coolers_on:  Dict[str, int]
    coolers_off:  Dict[str, int]
    waterpumps_on: Dict[str, int]
    waterpumps_off: Dict[str, int]
    created_at: datetime = datetime.now()


    class Config:
        schema_extra = {
        "example":{
        "rack_name": "comunication",
        "add_lights": {
            "light1": False,
            "light2": False,
            "light3": False,
            "light4": False
        },

        "add_coolers": {
            "coolers1": False,
            "coolers2": False,
            "coolers3": False,
            "coolers4": False
        },
        "add_waterpumps": {
            "waterpumps1": False,
            "waterpumps2": False
        },
        "add_electrovalvules": {

            "electrovalvule1": False,
            "electrovalvule2": False,
            "electrovalvule3": False
            "electrovalvule4": False

      },

    
        }
         }