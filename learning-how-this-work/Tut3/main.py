import time
from network import LoRa
import binascii

lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

while True:
    #The value can be a sensor reading being done here
    value = 5

    #Sending to pybytes in channel 1
    pybytes.send_signal(1, value)
    print("sending: {}".format(value))
    
    #Send every 5 seconds
    time.sleep(5)