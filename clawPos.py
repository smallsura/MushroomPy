#! /usr/local/bin/python

#Converts Joystick commands to move the coordinates of a point in 3D space

#Controls are assigned as such
# LStick controls movement along the x/y plane (the horizontal)
# Rstick controls movement along the z (vertical axis, and the claw rotation
# Pressing the Rstick opens or closes the gripper
# All this class needs to do is calculate a desirable position of the claw to be in. Further calculations are handled on the robot itself.


class clawPos:

	def calcPos(self, clawAt, joyValues):
		
		#clawAt is structured as follows
		# [x,y,z,rot,open]
		# rot is the angle of the claw
		# open is true or false

		#Flip the X axis, to make forward positive
		moveArmX = joyValues[13] * -1
		#Left is negative, right positive
		moveArmY = joyValues[12] 
		#Flip the Z axis, to make up positive
		moveArmZ = joyValues[15] * -1
		#Clockwise is positive, CCW is negative
		moveArmRot = joyValues[14] * 10
		#If RStick is pressed, open/close the claw
		changeClawState = joyValues[11]
		
		if changeClawState and clawAt[4]:
			clawAt[4] = False
			changeClawState = False
		
		if changeClawState and not clawAt[4]:
			clawAt[4] = True
		
		clawAt[0] = clawAt[0] + moveArmX
		clawAt[1] = clawAt[1] + moveArmY
		clawAt[2] = clawAt[2] + moveArmZ
		clawAt[3] = clawAt[3] + moveArmRot
		
		print clawAt

		return clawAt	
	



