#bin/python

pixel_count = 500

from neopixel import *

class Strip(object):
	def __init__(self, numPixels, brightness):
		self.numPixels = numPixels
		self.leds = Adafruit_NeoPixel(numPixels, 18, 800000, 5, False, brightness)
		self.leds.begin()
		self.clear()

	def clear(self):
		for x in xrange(self.numPixels):
			self.leds.setPixelColor(x, Color(0, 0, 0))
		self.leds.show()
	
if __name__ == "__main__":
	strip = Strip(pixel_count, 10)

