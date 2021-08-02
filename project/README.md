# The Door is open sensor
By:
Renato Opazo Salgado
ro222fd

In this tutorial, you will learn how to make a simple door sensor with a magnet sensor and some LED. This project will use WiFi to transmit data.

Estimated time: 2H

___


## Objective

### Why and what is the purpose?
I choose this project as a base for future projects to continue developing. And get a better understanding of how everything connects. As it will work as a base it can be developed into anything you want. As you want to know how many times the door is getting opened per day. Or maybe give out a warning if the door is open longer than it should be. Can be that you went on vacation and you see that your door gets opened while you were away? Then this project will give you the base to begin your first IoT project.

___


## Material

| | IoT Thing | For this | Price | Link |
| ----- |:---------- | --------- | ------ | ---------------- |
| ![Lopy4](https://pycom.io/wp-content/uploads/2018/08/lopySide-1.png) | Lopy4 | The LoPy4 is Micropython-programmable quadruple bearer board. Perfect way to start your project. | €38.45 | [Pycom](https://pycom.io/product/lopy4/) |
| ![Expansion Board](https://pycom.io/wp-content/uploads/2020/03/Website-Product-Shots-ExpB-Front.png) | Expansion board | It will be easier to code the Lopy4 and connect sensors to it with the expansion board. | €17.60 | [Pycom](https://pycom.io/product/expansion-board-3-0/) |
| ![USB](https://www.electrokit.com/uploads/productimage/41003/41003290.jpg) | Micro USB data cable | So you can connect the expansion board to the computer. | €4 | [Electrokit](https://www.electrokit.com/en/product/usb-cable-a-male-microb-male-1-8m/) |
| ![Breadboard](https://www.electrokit.com/uploads/productimage/41012/41012199-600x479.jpg) | Breadboard | It's a board there you can connect your sensors and cables before connecting it to the expansion board. | €6 | [Electrokit](https://www.electrokit.com/en/product/solderless-breadboard-400-tie-points/) |
| ![Jumper](https://www.electrokit.com/uploads/productimage/41003/41003181-600x450.jpg) | Jumper wires | You will need some to connect the sensor | €4 | [Electrokit](https://www.electrokit.com/en/product/hook-up-wires-w-pins-for-breadboard-smooth-65-pcs/) |
| ![Hall-effect](https://www.electrokit.com/uploads/productimage/41015/41015964-600x450.jpg) | Hall-effect sensor TLV49645 (Magnet Sensor) | To detect if the door is open or not. | €2 | [Electrokit](https://www.electrokit.com/en/product/tlv49645-sip-3-hall-effektsensor-digital-2/) |
| ![560ohm](https://www.electrokit.com/uploads/productimage/40811/40811256-600x180.png)| Resistor 560 Ohm | For the led | €0.3 X3 | [Electrokit](https://www.electrokit.com/produkt/motstand-metallfilm-0-6w-1-560ohm-560r/) |
| ![10Kohm](https://www.electrokit.com/uploads/productimage/41015/41015987-600x200.png)| Resistor 10K Ohm | For the hall effect sensor. | €0.3 | [Electrokit](https://www.electrokit.com/en/product/resistor-metal-film-0-125w-1-10kohm-10k/) |
| ![green-led](https://www.electrokit.com/uploads/productimage/41000/5mm-gr%C3%B6n-diffus-100x75.jpg)| Green LED | Just so we can have some status. Green for door close. | €0.15 | [Electrokit](https://www.electrokit.com/produkt/led-5mm-pure-gron-diffus/) |
| ![orange-led](https://www.electrokit.com/uploads/productimage/40300/5mm-orange-diffus-100x75.jpg)| Orange LED | Just so we can have some status. Orange for door open. | €0.3 | [Electrokit](https://www.electrokit.com/en/product/resistor-metal-film-0-125w-1-10kohm-10k/) |
| ![red-led](https://www.electrokit.com/uploads/productimage/40300/5mm-r%C3%B6d-diffus-100x75.jpg)| Red LED | Just so we can have some status. Red for door open to long. | €0.5 | [Electrokit](https://www.electrokit.com/en/product/resistor-metal-film-0-125w-1-10kohm-10k/) |
|![Magnet](https://www.electrokit.com/uploads/productimage/41011/41011479.jpg)| Magnet | To activate the sensor. You can use one from the kitchen or buy one tiny. | €5.5 | [Electrokit](https://www.electrokit.com/produkt/magnet-neo35-o10mm-x-8mm/) |



## Computer setup

| Type | Name |
| ---- |:------------------:|
| OS | Windows 10 |
| IDE | Visual Studio Code |

### A fast setup.

1. You should download and install [VS code](https://code.visualstudio.com/) if you don't have it in your PC.
2. You should also have installed [NodeJS](https://nodejs.org/en/) latest LTS version.
3. I didn't need to download any drivers but maybe you will need it. So follow this instructions [HERE](https://docs.pycom.io/gettingstarted/software/drivers/)
4. Before turning on the VS Code **we should do a Firmware update**. Download and install the updater from this [page](https://docs.pycom.io/updatefirmware/device/). Before you start the updater connect your LoPy4 to your expansion board and connect your Expansion board to your computer with the USB. If you are wandering how your Lopy4 and expansion board should be connected. The printed Logo Pycom on the both devices should be at the same side or see the image below. Now you can start the Pycom Firmware Updater and follow the instruction.
![pycom expansion board](https://docs.pycom.io/gitbook/assets/expansion_board_3_lopy4.png =x200)
5. Now you can start VS Code. We will **need a VS code plugin called Pymakr**. Here is the link to make it easy for you: [Pymakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr).
6. Now you are ready to code. Maybe you should **restart the VS Code** after installing the plugin.
7. **Notes**: The **Pymakr plugin** should find your device automatic. If it doesn't, check the pycom online documents. One more thing, the Lopy4 uses .py files and Micropython. The VS code will see that you are using Python files and will suggest to download and install **Python**. It will not be needed in this project as the **code will be compiled and used inside the Lopy4**.
8. Now you can **create your new project**. Don't be afraid to experiment. The Lopy4 is very forgiving.
9. You start by **creating two files** in your project folder. main.py and boot.py. Then a lib folder there you can put special libraries. In this project we will not use the lib folder.
10. When you have written your code you can test it by pressing the run button or the upload button in the bottom of VS code. ![run](https://docs.pycom.io/gitbook/assets/vsc_config_step_1-1.png)

### Pybytes, the 11th step.
Except for coloured LED, I will use Pybytes, a service from pycom to present my data. And I will transfer it through WiFi. This is a free service and it has an online editor that is also called Pymakr. If you use that then you can simply edit the files you have uploaded to your device or even delete the ones that you created by mistake.

It will simplify your life. Now just register here:

https://pybytes.pycom.io/

Just follow the [documentation](https://docs.pycom.io/pybytes/gettingstarted/) in their site and you will be fine to go.

___

## Putting everything together

![circuit](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/a372446fa4dd6d56fb31350647eb5a57bd21c151/circuit.png?token=ADMKLRHMTVA2BAUATZMFZXDBCB2CK)

In this image, the hall effect sensor is represented by a PNP transistor. The hall effect sensor has it flat side up. So the data cable is to the right and VCC is at the left. We have connected the data side to the PIN15 in the LoPy expansion board.

How I have it set up is not ready for production.
But if you want to take this to production you can use this circuit diagram. But instead of Lopy4, you could use a WiPy that is cheaper and then just buy a battery pack to power it and a generic chassis. Put some hole in it for LED and the sensor could be put in a sleeve so it gets closer to the magnet.


## The code


Here is the main part of the code. If you want to check the complete code look inside this [repo](https://github.com/TheRenato/1DT305-IoT/tree/main/project).
```python=
while True:
if (isMagnetActive(magnetPin())):
# Everything is fine becuase the door is close.
print("Everything is fine now")
ledSwitcher(1)
pybytes.send_signal(1, "Close")
while isMagnetActive(magnetPin()):
time.sleep(5)
else :
# We try to inform that the door is open.
print("The door is open")
ledSwitcher(2)
pybytes.send_signal(1, "Open")
counter = 0
while not (isMagnetActive(magnetPin())):
time.sleep(1)
counter = counter + 1
if (counter == 600):
# We warn that the door has been open some time now.
print("How long should it be open?")
ledSwitcher(3)
pybytes.send_signal(1, "Warning Open")

```

Here you can see that every event is the user informed in 3 ways. First in console, then by turning on a led and last by publishing it in the cloud to the Pycom service Pybytes.


## Transmitting the data/connectivity

The code sends data every time the hall effect sensor sense a change or the door has been open for 10 minutes.
It will be transmitted by WiFi and it will use MQTT.


Here is a image of the dashboard:
![image alt](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/pybytes-dashboard.png =x350)

## Finalizing the design

If you press on the image you will get the image in 4000x3000px.

Overview of the project:
[![overview](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_overview.jpg =x350)](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_overview.jpg)

Overview over the Lopy pins
[![pycom overview](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_overview_pycom.jpg =x350)](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_overview_pycom.jpg)

Overview of the LED and the rest of the breadboard.
[![breadboard overview](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/overview_breadboard.jpg =x350)](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/overview_breadboard.jpg)

Overview of the hall effect sensor(magnet sensor).
[![magnet overview](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_magnet_sensor.jpg =x350)](https://raw.githubusercontent.com/TheRenato/1DT305-IoT/main/real_magnet_sensor.jpg)


### Final Thoughts

The original project was more complex. But because of a faulty sensor, in the end, stoped me a bit I was forced to simplify. But it was fun and I learned a lot and will continue learning.