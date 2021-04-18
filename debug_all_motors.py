from multiprocessing import Process
from time import sleep
import RPi.GPIO as GPIO
from adafruit_mcp230xx.mcp23017 import MCP23017
import busio
import board
import digitalio

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c) 
GPIO.setmode(GPIO.BCM)

#### Motor directory ####
m4b_DIR = digitalio.DigitalInOut(board.D5)
m4b_DIR.direction = digitalio.Direction.OUTPUT

m4b_STEP = digitalio.DigitalInOut(board.D6)
m4b_STEP.direction = digitalio.Direction.OUTPUT

m4b_EN = digitalio.DigitalInOut(board.D12)
m4b_EN.direction = digitalio.Direction.OUTPUT

pancake_DIR = digitalio.DigitalInOut(board.D13)
pancake_DIR.direction = digitalio.Direction.OUTPUT

pancake_STEP = digitalio.DigitalInOut(board.D16)
pancake_STEP.direction = digitalio.Direction.OUTPUT

pancake_EN = digitalio.DigitalInOut(board.D19)
pancake_EN.direction = digitalio.Direction.OUTPUT

m1s_DIR = mcp.get_pin(15)
m1s_DIR .switch_to_output()

m1s_STEP = digitalio.DigitalInOut(board.D20)
m1s_STEP.direction = digitalio.Direction.OUTPUT

m1s_EN = digitalio.DigitalInOut(board.D21)
m1s_EN.direction = digitalio.Direction.OUTPUT

m3s_DIR = mcp.get_pin(12)
m3s_DIR .switch_to_output()

m3s_STEP = mcp.get_pin(13)
m3s_STEP .switch_to_output()

m3s_EN = mcp.get_pin(14)
m3s_EN .switch_to_output()


m1b_DIR = mcp.get_pin(2)
m1b_DIR .switch_to_output()

m1b_STEP = mcp.get_pin(3)
m1b_STEP .switch_to_output()

m1b_EN = mcp.get_pin(4)
m1b_EN .switch_to_output()

m2b_DIR = mcp.get_pin(8)
m2b_DIR .switch_to_output()

m2b_STEP = mcp.get_pin(0)
m2b_STEP .switch_to_output()

m2b_EN = mcp.get_pin(1)
m2b_EN .switch_to_output()

m2s_DIR = mcp.get_pin(9)
m2s_DIR .switch_to_output()

m2s_STEP = mcp.get_pin(10)
m2s_STEP .switch_to_output()

m2s_EN = mcp.get_pin(11)
m2s_EN .switch_to_output()

m4s_DIR = mcp.get_pin(5)
m4s_DIR .switch_to_output()

m4s_STEP = mcp.get_pin(6)
m4s_STEP .switch_to_output()

m4s_EN = mcp.get_pin(7)
m4s_EN .switch_to_output()

m3b_DIR = digitalio.DigitalInOut(board.D11)
m3b_DIR.direction = digitalio.Direction.OUTPUT

m3b_STEP = digitalio.DigitalInOut(board.D8)
m3b_STEP.direction = digitalio.Direction.OUTPUT

m3b_EN = digitalio.DigitalInOut(board.D7)
m3b_EN.direction = digitalio.Direction.OUTPUT

def test_motor(step_count, EN,  STEP, DIR):				# Main Motor loop definition
	EN.value = True				# enabling both motors
	DIR.value = False
	for x in range(step_count):			# Start of motor loop
		
		if 0 <= x <= 10:			# This ramps up the speed of the
			delay = 0.015			# steps by decreasing the delay
		if 10 <= x <= 20:			# between them. A long delay at
			delay = 0.013			# first is better for torque while
		if 20 <= x <= 30:			# a short delay is better for 
			delay = 0.011			# smooth turns!
		if x >= 30:
			delay = 0.01


		STEP.value = True			# main part of the normal motor step
		sleep(delay)				# delay changes based on above if's
		print(x)
		STEP.value = False
		sleep(delay)
		
	EN.value = False				# enabling both motors


