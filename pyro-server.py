#! /usr/local/bin/python

import Pyro4

class messageReceiver:

	def sendSpeed(self, speed):
		print speed

	def sendClawPos(self, clawAt):
		print clawAt


message_receiver = messageReceiver()


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(message_receiver)
ns.register("test.message", uri)

print "Good to go!"
daemon.requestLoop()



