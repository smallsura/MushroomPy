#! /usr/local/bin/python

###
# Talks to the SSC-32 Board on the Corobot.
# It sends the command strings in the format
# #[pin]P[Pulse Width]S[Speed(2000 here)]
###

import serial

class SSCHandler:

	def init(self):
		#port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
		#print port.portstr
		print "port open"

	def send(self, pin, pulseWidth):

		#port.write("#" + str(pin) + "P" + str(pulseWidth) + "S2000")		
		print("#" + str(pin) + "P" + str(pulseWidth) + "S2000")		
