#!/usr/bin/env python3


from multiprocessing import Process
from time import sleep
import RPi.GPIO as GPIO
from adafruit_mcp230xx.mcp23017 import MCP23017
import busio
import board

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)  # MCP23017
GPIO.setmode(GPIO.BCM)

CW = 1
CCW = 0
STEP = 0
# Setup Motors
# DIR, STEP, SLEEP/RST

motor_dictionary = {
	'm1b': [2, 3, 4],
	'm1s': [15, 20, 21],
	'm3b': [11, 8, 7],
	'm4b': [5, 6, 12]
	}
	
# ~ if ('m1b' | 'm2b' | 'm1b' | 'm2b') == motor_list:
	# ~ run code 
# ~ if in list_gpio:
# ~ if in list_mcp:
# ~ if motor_list == 'm1s':	
	

# ~ if dictionary == 'm1s'
	# ~ motor_dictionary_mcp(motor_dictionary[motor_list][2], EN).value = True # Turning on motor
	# ~ print("completed first motor: ", motor_dictionary[motor_list][2])
	# ~ GPIO.output(motor_dictionary[motor_list][0], DIR) # Sets Direction of motor
	# ~ print("completed first motor: ", motor_dictionary[motor_list][0])
	# ~ GPIO.output(motor_dictionary[motor_list][1], STEP) # Step on
	# ~ print("completed first motor: ", motor_dictionary[motor_list][1])
	# ~ EN = 0
	# ~ GPIO.output(motor_dictionary[motor_list][2], EN) # Turning off motor
	# ~ print("completed first motor: ", motor_dictionary[motor_list][2])

m1b = [mcp.get_pin(2) , mcp.get_pin(3), mcp.get_pin(4)] # MCP
m1s = [mcp.get_pin(15).switch_to_output(value=True), GPIO.setup(20, GPIO.OUT), GPIO.setup(21, GPIO.OUT)]
m2b = [mcp.get_pin(8), mcp.get_pin(0), mcp.get_pin(1)]
m2s = [mcp.get_pin(9), mcp.get_pin(10), mcp.get_pin(11)]
m3b = [GPIO.setup(11, GPIO.OUT), GPIO.setup(8, GPIO.OUT), GPIO.setup(7, GPIO.OUT)]
m3s = [mcp.get_pin(12), mcp.get_pin(13), mcp.get_pin(14)]
m4b = [GPIO.setup(5, GPIO.OUT), GPIO.setup(6, GPIO.OUT), GPIO.setup(12, GPIO.OUT)]
m4s = [mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7)]
pancake = [GPIO.setup(13, GPIO.OUT), GPIO.setup(16, GPIO.OUT), GPIO.setup(19, GPIO.OUT)]

mcp_list = ['m1b', 'm2b', 'm2s', 'm3s', 'm4s']
gpio_list = ['m3b', 'm4b', 'pancake']
# pin1 = mcp.get_pin(15)
# pin1.value = True
# GPIO.output(pin, 0/1)

# ~ mcp_pin2 = mcp.get_pin(2).switch_to_output

# ~ m1b[0].value = True
# once motor is run we cannot grab the pins, it prints [None, None, None]

def complete_motor(motor_list, DIR, num_of_steps, EN=1):
	print(motor_list, DIR, num_of_steps, EN)
	# dictionary['m3b'] = [DIR, STEP, EN] <--- Only pin numbers
	
	# ~ print(type(motor_list))
	# ~ print(motor_list)
	# MCP
	if motor_list in mcp_list: # run code for mcp
		
		# Setting up the pin output for Expander
		pin = mcp.get_pin(motor_dictionary[motor_list][0])
		
		print(pin)
		print('value ', pin.value)
		
		# Setting the value of the pin to true
		pin.switch_to_output(value=EN)
		
		print(pin)
		print('value ', pin.value)
		# Setting the value of the pin to true
		pin.switch_to_output(value=False)
		
		print('value ', pin.value)
		print('ran mcp code')
	# GPIO 	
	elif motor_list in gpio_list: # run code GPIO
		GPIO.output(motor_dictionary[motor_list][2], EN) # Turning on motor
		print("gave ", motor_dictionary[motor_list][2], 'the value ', EN)
		GPIO.output(motor_dictionary[motor_list][0], DIR) # Sets Direction of motor
		print("gave ", motor_dictionary[motor_list][0], 'the value ', DIR)
		GPIO.output(motor_dictionary[motor_list][1], STEP) # Step on
		print("gave ", motor_dictionary[motor_list][1], 'the value ', STEP)
		EN = 0
		GPIO.output(motor_dictionary[motor_list][2], EN) # Turning off motor
		print("gave ", motor_dictionary[motor_list][2], 'the value ', EN)
	
	elif motor_list == 'm1s' :
		# run half/half code
		print('ran half/half code')

	else:
		print('Error')

def motor_choice():
	motor = []
	num_of_motors = int(input("How many motors? "))
	for x in range(num_of_motors):
		motor_name = input("What Motor? ")
		motor.insert(x, motor_name)
	m3b
	m4b
	m1s
	print("Motors selected: ", motor)
	
	DIR = input("What Direction? ")
	if DIR == "CW":
		DIR = 1
	elif DIR == "CCW":
		DIR = 0
		
	num_of_steps = int(input("How many Steps? ")) 
	EN = (input("(E)nable or (D)isable? "))
	
	if EN == "E":
		EN = 1
	elif EN == "D":
		EN = 0
	
	for x in range(num_of_motors):
		complete_motor(motor[x], DIR, num_of_steps, EN)
	
	
motor_choice()



		# ~ print(pin1)
		# ~ print(type(pin1))
		# ~ print(motor_dictionary[motor_list][0])
		# ~ print(motor_dictionary['m1b'])
		# ~ print(type(motor_dictionary['m1b']))
		# ~ print(motor_dictionary[motor_list][0].value)
		# ~ print('first')
		# ~ motor_dictionary[motor_list][0].value = True
		# ~ print('second')
		# ~ print(motor_dictionary[motor_list][0].value)
		
		# ~ print(pin1)
		# ~ pin1.value = True
		# ~ motor_dictionary[motor_list][1].value = True
		# ~ print(motor_dictionary[motor_list][1])
		# ~ print(motor_dictionary[motor_list][1].value)
		# ~ m1b[1].value = True
		# ~ m1b[1].value = True
		# ~ motor_dictionary[motor_list][2]
		# ~ pin1.value = True
		
