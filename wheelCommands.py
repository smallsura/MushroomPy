#! /usr/local/bin/python

#Converts Joystick commands to send commands to the wheel system

class wheelCommands:
	
	#converts joy values to a speed coeficient. This will be used to multiply the max speed of the robot
	def joyToWheels(self, joyValues):
		
		#fowardSpeed is multiplied by -1 to make forward speed positive. The joystick has foward be negative by default.
		forwardSpeed = -1 * joyValues[13]
		rotationSpeed = joyValues[12]

		if joyValues[13] < 0:
			print "driving forwards, at speed: " + str(forwardSpeed)
		if joyValues[13] > 0:
			print "driving backwards, at speed: " + str(forwardSpeed)
		if joyValues[12] > 0:
			print "turning right, at speed: " + str(rotationSpeed)						
		if joyValues[12] < 0:
			print "turning left, at speed: " + str(rotationSpeed)
		if joyValues[13] == 0 and joyValues[12] == 0:
			print "stop!"

		speed = [forwardSpeed, rotationSpeed]
		return speed
