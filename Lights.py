import board
import neopixel

class Lights:
    def __init__(self):
        self.pixels = neopixel.NeoPixel(board.D18, 144, auto_write=False)

    def turn_on(self):
        self.pixels.fill((255, 255, 255))
        self.pixels.show()

    def turn_off(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()