import RPi.GPIO as GPIO
import pdb
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	data = reader.read()
	print("The ID is: ", data[0])

finally:
	GPIO.cleanup()
