from machine import Pin
import time
import pycom

pycom.heartbeat(False)

magnetPin = Pin('P15', mode=Pin.IN)
ledGreen = Pin('P22', Pin.OUT, pull = Pin.PULL_DOWN)
ledOrange = Pin('P21', Pin.OUT, pull = Pin.PULL_DOWN)
ledRed = Pin('P20', Pin.OUT, pull = Pin.PULL_DOWN)

def isMagnetActive(magnetValue):
    return magnetValue<1
def ledSwitcher(ledValue):
    if ledValue == 0:
        ledGreen.value(0)
        ledOrange.value(0)
        ledRed.value(0)
    elif ledValue == 1:
        ledGreen.value(1)
        ledOrange.value(0)
        ledRed.value(0)
    elif ledValue == 2:
        ledGreen.value(0)
        ledOrange.value(1)
        ledRed.value(0)
    elif ledValue == 3:
        ledGreen.value(0)
        ledOrange.value(0)
        ledRed.value(1)
    else:
        ledGreen.value(1)
        ledOrange.value(1)
        ledRed.value(1)

hello_world="Booting up"

print(hello_world)
ledSwitcher(4)
time.sleep(4)

while True:
  magnetValue = magnetPin()

  if (isMagnetActive(magnetPin())):
      print("Everything is fine now")
      ledSwitcher(1)
      pybytes.send_signal(1, "Close")
      while isMagnetActive(magnetPin()):
          time.sleep(5)
  else :
      print("The door is open")
      ledSwitcher(2)
      pybytes.send_signal(1, "Open")
      counter = 0
      while not (isMagnetActive(magnetPin())):
          time.sleep(1)
          counter = counter + 1
          if (counter == 600):
              print("How long should it be open?")
              ledSwitcher(3)
              pybytes.send_signal(1, "Warning Open")