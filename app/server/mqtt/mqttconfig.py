from fastapi_mqtt import FastMQTT, MQTTConfig
from  server.mqtt.secrets import secrets

mqtt_config = MQTTConfig(host= secrets["host"],    # mqtt config data
                         port= secrets["port"],
                         keepalive=60,
                         username= secrets["username"],
                         password= secrets["password"])


mqtt = FastMQTT(config=mqtt_config)          # recieve config data to create mqtt conection