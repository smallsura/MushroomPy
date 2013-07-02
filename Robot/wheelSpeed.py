#! /usr/local/bin/python

# Converts joystick commands to usable wheel commands

class wheelSpeed:

	def calculate(self, speed, PULSE_WIDTH_STOP):
		if speed[0] == 0:
			pulseWidth = PULSE_WIDTH_STOP
		elif speed[0] > 0:
			pulseWidth = 1200
		elif speed[0] < 0:
			pulseWidth = 1800

		return pulseWidth
