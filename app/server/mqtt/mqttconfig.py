from fastapi_mqtt import FastMQTT, MQTTConfig

mqtt_config = MQTTConfig(host="192.168.0.103",    # mqtt config data
                         port=1883,
                         keepalive=60,
                         username="noslen",
                         password="100loops")


mqtt = FastMQTT(config=mqtt_config)          # recieve config data to create mqtt conection