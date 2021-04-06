#!/usr/bin/env python3


from multiprocessing import Process
from time import sleep
import RPi.GPIO as GPIO
from adafruit_mcp230xx.mcp23017 import MCP23017

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)  # MCP23017
GPIO.setmode(GPIO.BCM)


# Setup Motors
# DIR, STEP, SLEEP/RST
m1b = [mcp.get_pin(2), mcp.get_pin(3), mcp.get_pin(4)]
m1s = [mcp.get_pin(15), GPIO.setup(20, GPIO.OUT), GPIO.setup(21, GPIO.OUT)]
m2b = [mcp.get_pin(8), mcp.get_pin(0), mcp.get_pin(1)]
m2s = [mcp.get_pin(9), mcp.get_pin(10), mcp.get_pin(11)]
m3b = [GPIO.setup(11, GPIO.OUT), GPIO.setup(8, GPIO.OUT), GPIO.setup(7, GPIO.OUT)]
m3s = [mcp.get_pin(12), mcp.get_pin(13), mcp.get_pin(14)]
m4b = [GPIO.setup(5, GPIO.OUT), GPIO.setup(6, GPIO.OUT), GPIO.setup(12, GPIO.OUT)]
m4s = [mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7)]
pancake = [GPIO.setup(13, GPIO.OUT), GPIO.setup(16, GPIO.OUT), GPIO.setup(19, GPIO.OUT)]


GPIO.output(, GPIO.HIGH)

GPIO.setup(

###### First motor ######
DIR1 = 4    # Direction GPIO Pin
STEP1 = 12  # Step GPIO Pin
#########################

###### Second motor ######
DIR2 = 17   # Direction GPIO Pin
STEP2 = 27  # Step GPIO Pin
#########################

###### Third motor ######
DIR3 = 6   # Direction GPIO Pin
STEP3 = 5  # Step GPIO Pin
#########################

###### Fourth motor ######
DIR4 = 26   # Direction GPIO Pin
STEP4 = 16  # Step GPIO Pin
#########################

###### Fifth motor ######
DIR5 = 20   # Direction GPIO Pin
STEP5 = 21  # Step GPIO Pin
#########################

###### Sixth motor ######
DIR6 = 14   # Direction GPIO Pin
STEP6 = 15  # Step GPIO Pin
#########################

###### Seventh motor ######
DIR7 = 13   # Direction GPIO Pin
STEP7 = 19  # Step GPIO Pin
#########################

###### 8th motor ######
DIR8 = 11   # Direction GPIO Pin
STEP8 = 9   # Step GPIO Pin
#########################

###### 9th motor ######
DIR9 = 8    # Direction GPIO Pin
STEP9 = 25  # Step GPIO Pin
#########################

DIR_list = [DIR1, DIR2, DIR3, DIR4, DIR5, DIR6, DIR7, DIR8, DIR9];
STEP_list = [STEP1, STEP2, STEP3, STEP4, STEP5, STEP6, STEP7, STEP8];

GPIO.setmode(GPIO.BCM)

###### First motor ######
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
#########################

###### Second motor ######
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

#########################

###### Third motor ######
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)

#########################

###### Fourth motor ######
GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)

#########################

###### Fifth motor ######
GPIO.setup(DIR5, GPIO.OUT)
GPIO.setup(STEP5, GPIO.OUT)

#########################

###### Sixth motor ######
GPIO.setup(DIR6, GPIO.OUT)
GPIO.setup(STEP6, GPIO.OUT)

#########################

###### Seventh motor ######
GPIO.setup(DIR7, GPIO.OUT)
GPIO.setup(STEP7, GPIO.OUT)

#########################

###### Eighth motor ######
GPIO.setup(DIR8, GPIO.OUT)
GPIO.setup(STEP8, GPIO.OUT)

#########################

###### Ninth motor ######
GPIO.setup(DIR9, GPIO.OUT)
GPIO.setup(STEP9, GPIO.OUT)

#########################

CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

def func1(DIR, STEP, step_count=SPR):
	#print('motor 1: starting')
	#for i in range(10000000): pass
	#print('motor 1: finishing')
    GPIO.output(DIR, CW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        print(x)
        GPIO.output(STEP, GPIO.LOW)
        
        sleep(delay)
    
    sleep(.5)
    #print("done")
    sleep(1)
    GPIO.output(DIR, CCW)
    #print("CCW")
    sleep(1)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)


def runInParallel(*fns):
	proc = []
	for fn in fns:
		p = Process(target=fn)
		p.start()
		proc.append(p)
	for p in proc:
		p.join()

def RunAllMotors():
	for x in range(len(DIR_list))
		runInParallel(func1(DIR_list[x], STEP_list[x], step_count=SPR))

motor_num = input("Which motor would you like to run, or enter '10' to run all motors ")

if (1 <= motor_num <= 9):
	runInParallel(func1(DIR_list[motor_num-1], STEP_list[motor_num-1], step_count=SPR))
	
if motor_num  == 10:
	RunAllMotors()
	
else:
	print("Please enter motor numbers 1 - 9")

GPIO.setup(23, GPIO.OUT)
pwm=GPIO.PWM(23, 50)
pwm.start(0)

def SetAngle(angle):
	print("start of def")
	duty = angle / 18 + 2
	GPIO.output(23, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(23, False)
	pwm.ChangeDutyCycle(0)
	print("end of def")
	
SetAngle(90)
sleep(.1)
SetAngle(180) 
sleep(.1)
SetAngle(90) 
sleep(.1)
pwm.stop()


GPIO.output(kelly, GPIO.LOW)
GPIO.cleanup()

