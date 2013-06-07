from IRCModule import *

class Test(IRCModule):
	filter = r"test"

	def on_filter(self, message):
		return "test keyword detected!"
