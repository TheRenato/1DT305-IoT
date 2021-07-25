from network import LoRa
import time
import binascii

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('937DA2C4D898CFF6497607DA72716D33')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')

# Your old code from main.py should be here