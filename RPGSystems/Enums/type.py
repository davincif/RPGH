from enum import Enum

class RSType(Enum):
	__order__ = "RSType is iterable"
	DND5 = 0 #D&D 5º edition

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.DND5:
			return "D&D 5th edition"
