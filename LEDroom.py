# Control neopixels from raspberry pi
# Author: Brian Aggrey (baggrey1@gmail.com)

from neopixel import *
import time, json

#LED strip configuration
STRIP_1_LED_COUNT         = 410
STRIP_1_GPIO_PIN          = 18
STRIP_1_LED_FREQ_HZ       = 800000
STRIP_1_DMA               = 5
STRIP_1_BRIGHTNESS        = 128
STRIP_1_INVERT            = False
STRIP_1_PWM_CHANNEL       = 0

STRIP_2_LED_COUNT         = 460
STRIP_2_GPIO_PIN          = 19
STRIP_2_LED_FREQ_HZ       = 800000
STRIP_2_DMA               = 5
STRIP_2_BRIGHTNESS        = 128
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
	with open('last_color.txt') as infile:    
		storedColor = json.load(infile)

	color = Color(storedColor['red'], storedColor['green'], storedColor['blue'])

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
	strip1.begin()
	strip2.begin()
	color = Color(0, 0, 0)

	# set pixel states for both strips
	for i in range(strip1.numPixels()):
		strip1.setPixelColor(i,color)

	for i in range(strip2.numPixels()):
		strip2.setPixelColor(i,color)

	# update strips
	strip1.show()
	strip2.show()

def setColor(red,green,blue):
	# this function sets color for all LEDS
	# initialize strips
	strip1.begin()
	strip2.begin()

	color = Color(red, green, blue)

	# set pixel states for both strips
	for i in range(strip1.numPixels()):
		strip1.setPixelColor(i,color)

	for i in range(strip2.numPixels()):
		strip2.setPixelColor(i,color)

	#update strips
	strip1.show()
	strip2.show()

def fade(state):
	# this function fades the lights on to the stored color
	# initialize strips
	strip1.begin()
	strip2.begin()

	# set fade options in s
	fadeDuration = .1
	fadeResolution = .005
	fadeSteps = int(fadeDuration/fadeResolution)

	# initialize color step:
	colorStep = {
		'red': 1,
		'green': 1,
		'blue' : 1
	}

	offColor = {
		'red': 0,
		'green': 0,
		'blue': 0
	}

	# define color
	with open('last_color.txt') as infile:    
		storedColor = json.load(infile)

	if state == 'on':
		startColor = offColor
		endColor = storedColor

	else:
		startColor = storedColor
		endColor = offColor

	for i in range(1,fadeSteps):
		for component in endColor:
			# set color components for step
			colorComponentDiff = endColor[component]-startColor[component]
			colorStep[component] = startColor[component] + int(colorComponentDiff*fadeResolution/fadeDuration*i)
		
		# instantiate color object
		print(colorStep)
		color = Color(colorStep['red'], colorStep['green'], colorStep['blue'])

		for k in range(strip1.numPixels()):
			strip1.setPixelColor(k,color)

		for k in range(strip2.numPixels()):
			strip2.setPixelColor(k,color)

		# update strips
		strip1.show()
		strip2.show()

		# wait for duration of step
		time.sleep(fadeResolution)
