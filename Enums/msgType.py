from enum import Enum

class MsgType(Enum):
	INFO = 0
	QUESTION = 1
	WARNING = 2
	ERROR = 3

	#OVERWRITE METHODS
	def __str__(self):
		if self.value == self.INFO:
			back = "Information"
		elif self.value == self.ERROR:
			back = "Error"
		elif self.value == self.WARNING:
			back = "Warning"
		elif self.value == self.QUESTION:
			back = "Question"
		else:
			back = "Incorret error value"

		return back

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value
