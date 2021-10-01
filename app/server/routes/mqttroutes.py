rack_db = {}

# susbcribe to the topic on conecct to the mqtt broker
@mqtt.on_connect()
def connect(client, flags, rc, properties):
    mqtt.client.subscribe("microstation")  # subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

# recieve mqtt message
@mqtt.on_message()
async def mqtt_message(client, topic, payload, qos, properties):

    # decode json data from payload
    mqtt_decode = str(payload.decode("utf-8", "ignore"))
    # convert into python dictionary
    convert_mqtt_json = json.loads(mqtt_decode)
    for key in convert_mqtt_json.keys():  # create new dictionary to changes keys

        global rack_db

        val = convert_mqtt_json[key]  # saves keys into val variable
        # saves ambient temperature_1 in a variable
        ambient_temperature_1_recieve = val.get('AT1')
        # saves ambient temperature_1 in a dictionary
        rack_db["ambient_temperature_1"] = ambient_temperature_1_recieve

        ambient_temperature_2_recieve = val.get('AT2')
        rack_db["ambient_temperature_2"] = ambient_temperature_2_recieve

        ambient_humydity_1_recieve = val.get('AH1')
        rack_db["ambient_humidity_1"] = ambient_humydity_1_recieve

        ambient_humydity_2_recieve = val.get('AH2')
        rack_db["ambient_humidity_2"] = ambient_humydity_2_recieve

        soil_humydity_1a_recieve = val.get('SH1a')
        rack_db["soil_humydity_1a"] = soil_humydity_1a_recieve

        soil_humydity_1b_recieve = val.get('SH1b')
        rack_db["soil_humydity_1b"] = soil_humydity_1b_recieve

        soil_humydity_2a_recieve = val.get('SH2a')
        rack_db["soil_humydity_2a"] = soil_humydity_2a_recieve

        soil_humydity_2b_recieve = val.get('SH2b')
        rack_db["soil_humydity_2b"] = soil_humydity_2b_recieve

        water_temperature_micros_recieve = val.get('WTM')
        rack_db["water_temperature_microgreens"] = water_temperature_micros_recieve

        water_temperature_hydroponics_recieve = val.get('WTH')
        rack_db["water_temperature_hydroponics"] = water_temperature_hydroponics_recieve

        water_level_microgreens_recieve = val.get('WLT1')
        rack_db["water_level_microgreens"] = water_level_microgreens_recieve

        water_level_hydroponics_recieve = val.get('WLT2')
        rack_db["water_level_hydroponics"] = water_level_hydroponics_recieve

        water_level_tray_1_recieve = val.get('WLT1')
        rack_db["water_level_tray_1 "] = water_level_tray_1_recieve

        water_level_tray_2_recieve = val.get('WLT2')
        rack_db["water_level_tray_2"] = water_level_tray_2_recieve

        print("Received message: ", topic, payload.decode(), qos, properties)
        return rack_db
        # json_data = json.dumps (mqtt_decode)


# mqtt disconnect info
@mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

# mqtt subscribe info
@mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)
