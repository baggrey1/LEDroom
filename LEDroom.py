# Control neopixels from raspberry pi
# Author: Brian Aggrey (baggrey1@gmail.com)

import time
from neopixel import *

#LED strip configuration
STRIP_1_LED_COUNT         = 410
STRIP_1_GPIO_PIN          = 18
STRIP_1_LED_FREQ_HZ       = 800000
STRIP_1_DMA               = 5
STRIP_1_BRIGHTNESS        = 255
STRIP_1_INVERT            = False
STRIP_1_PWM_CHANNEL       = 0

STRIP_2_LED_COUNT         = 460
STRIP_2_GPIO_PIN          = 19
STRIP_2_LED_FREQ_HZ       = 800000
STRIP_2_DMA               = 5
STRIP_2_BRIGHTNESS        = 255
STRIP_2_INVERT            = False
STRIP_2_PWM_CHANNEL       = 1

def updateAll(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i,color)
	strip.show()

def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

if __name__ == '__main__':
	strip1 = Adafruit_NeoPixel(STRIP_1_LED_COUNT, STRIP_1_GPIO_PIN, STRIP_1_LED_FREQ_HZ, STRIP_1_DMA, STRIP_1_INVERT, STRIP_1_BRIGHTNESS, STRIP_1_PWM_CHANNEL)
	strip2 = Adafruit_NeoPixel(STRIP_2_LED_COUNT, STRIP_2_GPIO_PIN, STRIP_2_LED_FREQ_HZ, STRIP_2_DMA, STRIP_2_INVERT, STRIP_2_BRIGHTNESS, STRIP_2_PWM_CHANNEL)

	strip1.begin()
	strip2.begin()
	updateAll(strip1, Color(255,0,0))
	updateAll(strip2, Color(0,255,0))
	while True:
		colorWipe(strip1, Color(255,0,0))
		colorWipe(strip2, Color(255,0,0))
		colorWipe(strip1, Color(0,255,0))
		colorWipe(strip2, Color(0,255,0))
		colorWipe(strip1, Color(0,0,255))
		colorWipe(strip2, Color(0,0,255))


