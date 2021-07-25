import machine
import time

adc = machine.ADC(bits=10)
apin = adc.channel(pin='P16')


while True:
  millivolts = apin.voltage()
  voltage = millivolts * (5 / 1024.0)
  celsius = (millivolts - 500) / 10.0

  print(celsius)
  
  time.sleep(1)