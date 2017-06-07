from enum import Enum

class MsgType(Enum):
	INFO = 0
	QUESTION = 1
	WARNING = 2
	ERROR = 3

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value
