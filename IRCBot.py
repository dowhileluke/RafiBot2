from IRCConnection import *

NICKNAME = "rafi2"
CHANNEL = "#rafidev"

class IRCBot:

	modules = []

	def attach(self, module):
		self.modules.append(module)
		return self

	def run(self):
		conn = IRCConnection(NICKNAME, CHANNEL)

		while True:
			message = conn.get_message() # convert to IRCMessage
			print message # debug

			for module in self.modules:
				response = module.process(message) # eventually should be an instance of IRCMessage
				if response is not None:
					print "--> " + response # debug
					conn.send_message("PRIVMSG {0} :{1} \r\n".format(CHANNEL, response))
