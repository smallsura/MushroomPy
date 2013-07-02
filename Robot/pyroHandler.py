#! /usr/local/bin/python

import Pyro4

class messageReceiver:

	def init(self, robotMain):

		daemon = Pyro4.Daemon()
		ns = Pyro4.locateNS()
		uri = daemon.register(robotMain)
		ns.register("test.message", uri)
		print "Good to go!"
		daemon.requestLoop()

#	def sendSpeed(self, speed):
#		print speed
#
#	def sendClawPos(self, clawAt):
#		print clawAt
#




