#bin/python

pixel_count = 339 
default_brightness = 250

import time
from neopixel import *

if __name__ == "__main__":
	print "hello"

	leds = Adafruit_NeoPixel(pixel_count, 18, 800000, 5, False, default_brightness)
	leds.begin()

	for x in range(pixel_count):
		print "count"
		print x
		leds.setPixelColor(x, Color(255, 255, 255))
		leds.show()
		time.sleep(0.05)

