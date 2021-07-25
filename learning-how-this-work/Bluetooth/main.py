from network import Bluetooth
import pycom
import time
import ubinascii

pycom.heartbeat(False)
bluetooth = Bluetooth()
bluetooth.set_advertisement(name="LoPy4", service_uuid=b'1234567890123456', manufacturer_data="lopy_v1", service_data="Hi world")

# some from: https://forum.pycom.io/topic/6994/find-my-phone-bluetooth-with-my-lopy4/2
def conn_cb (bt_o):
    events = bt_o.events()   # this method returns the flags and clears the internal registry

    if events & Bluetooth.CLIENT_CONNECTED:
        print("Client connected")
        #print(bt_o.get_adv())
        pycom.rgbled(0x001100)
        adv = bt_o.get_adv()
        print("All adv data: ",adv)
        if adv:
            print("mac: ", ubinascii.hexlify(adv.mac))
            print("data: ", ubinascii.hexlify(adv.data))

            # try to get the complete name
            print("Name: ", bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))

            mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
            if mfg_data:
                # try to get the manufacturer data (Apple's iBeacon data is sent here)
                print(ubinascii.hexlify(mfg_data))
        time.sleep(3)
        # bluetooth.disconnect_client()
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print("Client disconnected")
        pycom.rgbled(0x110000)
        time.sleep(10)
        pycom.heartbeat(True)
        pycom.heartbeat(False)

bluetooth.callback(trigger=Bluetooth.NEW_ADV_EVENT | Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)