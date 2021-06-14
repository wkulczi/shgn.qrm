import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P3)

while True:
    print("{} {}v\t\t{} {}v".format(chan0.value, chan0.voltage,chan1.value, chan1.voltage))
    time.sleep(0.5)
