# Control neopixels from raspberry pi
# Author: Brian Aggrey (baggrey1@gmail.com)

from neopixel import *

#LED strip configuration
STRIP_1_LED_COUNT         = 410
STRIP_1_GPIO_PIN          = 18
STRIP_1_LED_FREQ_HZ       = 800000
STRIP_1_DMA               = 5
STRIP_1_BRIGHTNESS        = 64
STRIP_1_INVERT            = False
STRIP_1_PWM_CHANNEL       = 0

STRIP_2_LED_COUNT         = 460
STRIP_2_GPIO_PIN          = 19
STRIP_2_LED_FREQ_HZ       = 800000
STRIP_2_DMA               = 5
STRIP_2_BRIGHTNESS        = 64
STRIP_2_INVERT            = False
STRIP_2_PWM_CHANNEL       = 1

strip1 = Adafruit_NeoPixel(STRIP_1_LED_COUNT, STRIP_1_GPIO_PIN, STRIP_1_LED_FREQ_HZ, STRIP_1_DMA, STRIP_1_INVERT, STRIP_1_BRIGHTNESS, STRIP_1_PWM_CHANNEL)
strip2 = Adafruit_NeoPixel(STRIP_2_LED_COUNT, STRIP_2_GPIO_PIN, STRIP_2_LED_FREQ_HZ, STRIP_2_DMA, STRIP_2_INVERT, STRIP_2_BRIGHTNESS, STRIP_2_PWM_CHANNEL)


def boringOn():
	# this function turns all the LEDs on to a normal room lighting color
	# initialize strips
	strip1.begin()
	strip2.begin()

	# define color
	color = Color(255, 207, 44)

	# set pixel states for both strips
	for i in range(strip1.numPixels()):
		strip1.setPixelColor(i,color)

	for i in range(strip2.numPixels()):
		strip2.setPixelColor(i,color)

	# update strips
	strip1.show()
	strip2.show()

def allOff():
	# this function turns all the LEDs in both strips off
	color = Color(0, 0, 0)

		# set pixel states for both strips
	for i in range(strip1.numPixels()):
		strip1.setPixelColor(i,color)

	for i in range(strip2.numPixels()):
		strip2.setPixelColor(i,color)

	# update strips
	strip1.show()
	strip2.show()
