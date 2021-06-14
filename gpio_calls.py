#randomy na razie
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from w1thermsensor import W1ThermSensor, Sensor

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chans = [AnalogIn(ads, ADS.P0), AnalogIn(ads,ADS.P3)]

def query_water_temp_mock():
    import random
    return round(15 + (40-15)*random.random(),2)

def query_light_mock():
    import random
    return random.randint(1,1024)

def query_light(all=True):
    #jeszcze nie wiem jak zrobie osobne
    avg = 0
    avg_voltage = 0
    if all:
        for element in chans:
            avg = avg + element.value
            avg_voltage = avg_voltage + element.voltage
    return {"val": int(avg/len(chans)), "voltage": round((avg_voltage/len(chans)),2)}

def query_water_temp():
    sensor = W1ThermSensor(sensor_type=Sensor.DS18B20)
    return round(sensor.get_temperature(),2)
