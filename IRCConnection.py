import socket
import re

class IRCConnection:
	connection = None
	ping = re.compile(r"^PING ")

	def __init__(self, nickname, channel):
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect(("irc.freenode.net", 6667))
		conn.send("NICK {0}\r\n".format(nickname))
		conn.send("USER {0} 0 * :{0}\r\n".format(nickname))
		conn.send("JOIN {0}\r\n".format(channel))
		self.connection = conn

	def get_message(self):
		while True:
			message = self.connection.recv(4096)

			if self.ping.search(message):
				self.connection.send("PONG {0}\r\n".format(message.split()[1]))
				print "ping/pong"
			else:
				return message

	def send_message(self, message):
		self.connection.send(message)

	def close(self):
		self.connection.close()
