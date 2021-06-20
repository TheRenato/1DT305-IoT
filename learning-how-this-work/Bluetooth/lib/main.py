import network
import pycom

pycom.heartbeat(False)

bluetooth = network.Bluetooth()

# If you haven't stopped the Bluetooth
# connection before running this code.
# This will do the work.
bluetooth.stop_scan()
bluetooth.start_scan(-1)  # start scanning with no timeout

count = 0

while (count<10):

    get_adv = bluetooth.get_adv()
    
    if get_adv :
        print("Device", count,": ")
        print("----")
        print(bluetooth.resolve_adv_data(get_adv.data, network.Bluetooth().ADV_NAME_CMPL))
        print("----")
        print(get_adv.mac)
        print("----")
        print(bluetooth.ADV_NAME_CMPL)
        print("----")
        print(get_adv.data)
        print("----")
        pycom.rgbled(0x221100)
        count = count + 1 
    
bluetooth.stop_scan()
pycom.heartbeat(False)