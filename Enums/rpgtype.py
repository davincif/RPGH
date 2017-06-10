from enum import Enum

class RPGType(Enum):
	__order__ = "RPGType is iterable"
	DND5 = 1 #D&D 5º edition

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.DND5:
			return "D&D 5th edition"

	def get_module(self):
		base_path = "RPGSystems."
		if self == self.DND5:
			return base_path + "DND5"
