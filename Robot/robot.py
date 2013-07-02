#! /usr/local/bin/python

###
# Main loop on the Robot side
#
# 1. Starts the Pyro listener
# 2. Waits for commands from client
# 3. Enacts command
###


###
# Import local classes
###
import pyroHandler
import wheelSpeed
#import inverseKinematics
import SSCHandler

###
# Import Python Libraries
###

###
# Set Constants
###
#Pulse width at which the wheel motors do not rotate
PULSE_WIDTH_STOP = 1470
MAX_WHEEL_SPEED = 2500

###
# Inititalise Variables
###
pulseWidth = PULSE_WIDTH_STOP
###
# Holds function calls to other classes
###

class robot:

	def sendSpeed(self, speed):	
		pulseWidth = moveWheels.calculate(speed, PULSE_WIDTH_STOP)		
		SSC32.send(0, pulseWidth)
		SSC32.send(1, pulseWidth)
	def sendClawPos(self, clawAt):
		print clawAt


###
# Start pyro listener
###
robotCommands = robot()
SSC32 = SSCHandler.SSCHandler()
SSC32.init()
moveWheels = wheelSpeed.wheelSpeed()
messageHandler = pyroHandler.messageReceiver()
messageHandler.init(robotCommands)

###
# Instantiate objects




