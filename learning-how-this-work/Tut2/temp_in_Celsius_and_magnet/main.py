import machine
from machine import Pin
import time

adc = machine.ADC(bits=10)
adcMagnet = machine.ADC()
tempPin = adc.channel(pin='P16')
# magnetPin = adcMagnet.channel(pin='P15')
magnetPin = Pin('P15', mode=Pin.IN)


while True:
  # Tempeture:
  millivolts = tempPin.voltage()
  voltage = millivolts * (5 / 1024.0)
  celsius = (millivolts - 500) / 10.0

  #  Magnet
  magnetValue = magnetPin()

  # Print Out
  print("Time:",time.asctime( time.localtime(time.time()) ))
  print("Celsius: ",celsius)
  print("Magnet: ",magnetValue)
  
  time.sleep(5)