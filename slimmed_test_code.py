from debug_all_motors import *


#### Motor Lists #####

step_motor = [m4b_STEP, pancake_STEP, m1s_STEP, m3s_STEP, m1b_STEP, 
				m2b_STEP, m2s_STEP, m4s_STEP, m3b_STEP]
				
dir_motor = [m4b_DIR, pancake_DIR, m1s_DIR, m3s_DIR, m1b_DIR, 
				m2b_DIR, m2s_DIR, m4s_DIR, m3b_DIR]
				
enable_motor = [m4b_EN, pancake_EN, m1s_EN, m3s_EN, m1b_EN, 
				m2b_EN, m2s_EN, m4s_EN, m3b_EN]


def motor_loop(step_count):			# Main Motor loop definition
	
	for x, item in enumerate(enable_motor):
		enable_motor[x].value = True

	for x in range(step_count):		# Start of motor loop
		
		if 0 <= x <= 10:			# This ramps up the speed of the
			delay = 0.015			# steps by decreasing the delay
		if 10 <= x <= 20:			# between them. A long delay at
			delay = 0.013			# first is better for torque while
		if 20 <= x <= 30:			# a short delay is better for 
			delay = 0.011			# smooth turns!
		if x >= 30:
			delay = 0.01
			
		for y, item in enumerate(step_motor):
			step_motor[y].value = True
		
		sleep(delay)				# delay changes based on above if's
		
		for z, item in enumerate(step_motor):
			step_motor[z].value = False
			
		print(x)

		sleep(delay)


try:
	while True:									# constant program
		user_input = input("how many steps? ")
			
		if user_input == "e":			# enable motors
			
			for x, item in enumerate(step_motor):
				enable_motor[x].value = True
			
		elif user_input == "d":			# disable motors
			
			for x, item in enumerate(step_motor):
				enable_motor[x].value = False
		
		elif user_input:  
			
			for x, item in enumerate(step_motor): # enable motors and delay 
				enable_motor[x].value = True  # before stepping
			
			sleep(.5)
			motor_loop(int(user_input))	# calling the motor loop
			
		elif not user_input:
			
			print("Re-running 10 steps")
			
			for x, item in enumerate(step_motor):
				enable_motor[x].value = True
			
			sleep(.8)
			motor_loop(10)
			
		else:							# if you type nothing, insult!
			
			print("type somethin' dum dum!")
			
except KeyboardInterrupt:	# Exit program
	
	print('\nYou pressed ctrl-c. The pins will now be reset')
			
	for x, item in enumerate(step_motor):
		enable_motor[x].value = False
