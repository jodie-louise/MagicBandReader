from mfrc522 import SimpleMFRC522
from MagicBandIds import ids as magic_band_ids

class RFIDReader:
    
    def read(self):
        reader = SimpleMFRC522()
        data = reader.read()
        read_id = data[0]

        if read_id in magic_band_ids.values():
            print("The ID is: ", read_id)
            return True
        else:
            return False
