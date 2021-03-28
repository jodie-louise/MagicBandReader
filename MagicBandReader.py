from RFIDReader import RFIDReader
from Lights import Lights
import RPi.GPIO as GPIO
import time

def run():
    print("Tap your magic band!")

    rfid_reader = RFIDReader()
    lights = Lights()

    if rfid_reader.read() == True:
        lights.turn_on()
        time.sleep(2)
        lights.turn_off()

if __name__ == '__main__':
    try:
        run()

    finally:
        GPIO.cleanup()