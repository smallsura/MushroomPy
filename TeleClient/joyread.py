#! /usr/local/bin/python

import pygame
import time

class joyread:
	
	#### Constants
	# Sets the control mode: 1 is arm control, 0 is wheel control
	CONTROL_MODE = 0 
	# Avoids the program interpreting a single press as multiple presses of the switch
	PREVIOUS_MODE = 0
		
	
	#gets everything running, returns the first joystick object after starting it	
	def init(self):
		pygame.init()
		pygame.joystick.init()
	
			
		joystick_count = pygame.joystick.get_count()
	
		for i in range(joystick_count):
			joystick = pygame.joystick.Joystick(i)
			joystick.init()
			break
		return joystick
	

	#grabs the last event, packs all the button/axes values into a list
	def getUpdate(self, joystick):
		
		values = []
	        for event in pygame.event.get():	
			buttons = joystick.get_numbuttons()
			for i in range( buttons ):
				button = joystick.get_button( i )
			#	if values.length
				values.append(button)
			# fetch joystick values. "i" is the axis number, "axis" is the value
			axes = joystick.get_numaxes()
			for i in range( axes ):
				axis = joystick.get_axis( i )
			# program in a deadzone to take care of dodgy calibration
				if axis < 0.12 and axis > -0.12:
					axis = 0
				values.append(axis)
			# print out axes values in case we need to check
			#print "Axis {} value: {:>6.3f}".format(i, axis)
			
		# fetch hat values (directional pad)
			hats = joystick.get_numhats()
        		for i in range( hats ):
            			hat = joystick.get_hat( i )
				values.append(hat)
			# Convert joystick values to desirable 3D space coordinates	
			# Assuming Logitech Rumblepad 2
			# Mappings are:
			# Axis 0 is LStick from Left -1 to Right 1
			# Axis 1 is LStick from Up -1 to Down 1
			# Axis 2 is RStick from Left -1 to Right 1
			# Axis 3 is Rstick from Up -1 to Down -1 
			
			# Button 9 [Labelled 10 on the controller] is used to switch between ARM CONTROL and WHEEL CONTROL modes
			# These need to be clearly labelled on screen to avoid confusion
			break
			#Final list is formatted like this:
		#[Buttons 0-10, LJoyPress, RJoyPress, Axes 0-3, D-Pad]
		#Note that if there is no event, the list is of length 0
			
		# print values
		return values
	
