from fastapi import FastAPI
from fastapi_mqtt import FastMQTT, MQTTConfig
from server.routes.growRoutes import router as Router
from server.mqtt.mqttconfig import mqtt
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()                                   # fast api app

origins = [
    "http://localhost:3000",
]

app.add_middleware(                             # add middleware to comunications with other apps
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


mqtt.init_app(app)                                # init mqtt service in fastapi
app.include_router(Router)



