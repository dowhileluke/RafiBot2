import re

class IRCModule:
	filter = None

	def __init__(self):
		if self.filter is not None:
			self.filter = re.compile(self.filter)

	def process(self, message):
		if self.filter is None or self.filter.search(message):
			return self.on_filter(message)

	def on_filter(self, message):
		pass
