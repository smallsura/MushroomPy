#! /usr/local/bin/python

#Client-side main

# 1. Read-in joystick commands [joyread.py]
# 2. Either:
# 2a. Convert to usable 3D coordinates [clawpos.py]
# 2b. Convert input to wheel commands [wheelCommands.py]
# 3. Pass on to robot


###
#Importing local classes
###
import joyread
import wheelCommands
import clawPos

###
#Importing python libraries
###
import time
import Pyro4

###
#init constants
###
SLEEP_TIME = 0.02

###
#init variables
###
wheelMode = True
joyValues = []
#speed is structured as follows:
# [forwardSpeed, Rotatiopn Speed]
speed = [0,0]
#clawAt is structured as follows:
# [x,y,z,rot,open]
# rot is the angle of the claw in degrees
# open is true or false
clawAt = [0,0,0,0,True]

###
#create objects from local classes
###
readin = joyread.joyread()
wheelCommander = wheelCommands.wheelCommands()
clawCalc = clawPos.clawPos()

###
#Open comms with the Pyro server
###
messageHandler = Pyro4.Proxy("PYRONAME:test.message")

###
#initialise the joystick capture
###
joystick = readin.init()

while 1:

	joyValues = readin.getUpdate(joystick)
	
	#if there are no updates, assume controller status has not change	
	if len(joyValues) == 0:
		joyValues = lastJoyValues
	else:
		lastJoyValues = joyValues

	#if the list is empty, no need to process it (only likely to happen at start before any commands are sent)
	if len(joyValues) == 0:
		time.sleep(SLEEP_TIME)
		continue 

	#check to see if control mode changed
	if joyValues[9] == 1:
		if wheelMode:
			wheelMode = False
			print "Switched to arm mode"
		else: 
			wheelMode = True 
			print "Switched to wheel mode"
	
	#If Wheel Mode, call wheelCommands
	if wheelMode:
		speed = wheelCommander.joyToWheels(joyValues)
		messageHandler.sendSpeed(speed)


	#If Arm Mode, call clawPos
	if not wheelMode:
		clawAt = clawCalc.calcPos(clawAt, joyValues)
		messageHandler.sendClawPos(clawAt)

	time.sleep(SLEEP_TIME)	

