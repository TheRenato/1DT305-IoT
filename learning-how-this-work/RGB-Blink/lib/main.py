import pycom
import time

pycom.heartbeat(False)
count = 0

while (count<10):
    #colors in hexadecimal (0xRRGGBB)
    pycom.rgbled(0x441100)  # Red
    time.sleep(1)
    pycom.rgbled(0x001100)  # Greenma
    time.sleep(1)
    pycom.rgbled(0x000011)  # Blue
    time.sleep(1)
    count = count + 1

pycom.heartbeat(False)