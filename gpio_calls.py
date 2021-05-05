#randomy na razie

from w1thermsensor import W1ThermSensor, Sensor

def query_water_temp_mock():
    import random
    return random.random(15,40)

def query_light_mock():
    import random
    return random.randint(1,1024)

def query_water_temp():
    sensor = W1ThermSensor(sensor_type=Sensor.DS18B20)
    return sensor.get_temperature()
