import RPi.GPIO as GPIO
import pdb
from mfrc522 import SimpleMFRC522
from MagicBandIds import ids as magic_band_ids

reader = SimpleMFRC522()

try:
	data = reader.read()
	read_id = data[0]
	
	if read_id in magic_band_ids.values():
		print("The ID is: ", read_id)

finally:
	GPIO.cleanup()
