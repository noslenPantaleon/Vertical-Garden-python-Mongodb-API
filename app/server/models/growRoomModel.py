import string
from pydantic import BaseModel, ValidationError, conint
from typing import Optional, Text, List, Dict
from time import time
from datetime import datetime


# model to create a new cycle plant
class Growcycle (BaseModel):
    growroom_name: str
    add_plants: Dict[str, str]


# model to create a new rack
class Growroom (BaseModel):

    growroom_name: str
    add_lights: Dict[str, bool]
    add_coolers:  Dict[str, bool]
    add_waterpumps: Dict[str, bool]
    add_electrovalvules: Dict[str, bool]
    add_sensors: Dict[str, str]
    add_plants:Dict[str, str]
    created_at: datetime = datetime.now()
    germinated: datetime = datetime.now()
    finish_germinated_cycle: datetime = datetime.now()
    growprocess:datetime = datetime.now()
    finish_grow: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example":{  
        "growroom_name": "str",

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
            "electrovalvule3": False,
            "electrovalvule4": False

      },

        "add_sensors": {
            "sensor1": "AmbientHumidity",
            "sensor2": "AmbientHumidity",
            "sensor3": "soilHumidity",
            "sensor4": "AmbientTemp"
          },

        "add_plants": {
            "plant1": "microgreenRucula",
            "plant2": "microgreenAlbahaca",
            "plant3": "microgreenMostaza",
            "plant4": "microgreenRabanito"
        },
        "created_at": "2022-06-27T20:56:35.762469",
        "germinated": "2022-06-27T20:56:35.762469",
        "finish_germinated_cycle": "2022-06-27T20:56:35.762469",
        "growprocess": "2022-06-27T20:56:35.762469",
        "finish_grow": "2022-06-27T20:56:35.762469"
    
       }
            }



 
# model to update an existent rack
class GrowroomUpdate (BaseModel):


    growroom_name: str
    add_lights: Dict[str, bool]
    add_coolers:  Dict[str, bool]
    add_waterpumps: Dict[str, bool]
    add_electrovalvules: Dict[str, bool]
    add_sensors: Dict[str, str]
    add_plants:Dict[str, str]
    created_at: datetime = datetime.now()
    germinated: datetime = datetime.now()
    finish_germinated_cycle: datetime = datetime.now()
    growprocess:datetime = datetime.now()
    finish_grow: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example":{  
        "growroom_name": "str",

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
            "electrovalvule3": False,
            "electrovalvule4": False

      },

        "add_sensors": {
            "sensor1": "AmbientHumidity",
            "sensor2": "AmbientHumidity",
            "sensor3": "soilHumidity",
            "sensor4": "AmbientTemp"
          },

        "add_plants": {
            "plant1": "microgreenRucula",
            "plant2": "microgreenAlbahaca",
            "plant3": "microgreenMostaza",
            "plant4": "microgreenRabanito"
        },
        "created_at": "2022-06-27T20:56:35.762469",
        "germinated": "2022-06-27T20:56:35.762469",
        "finish_germinated_cycle": "2022-06-27T20:56:35.762469",
        "growprocess": "2022-06-27T20:56:35.762469",
        "finish_grow": "2022-06-27T20:56:35.762469"
    
       }
            }










    