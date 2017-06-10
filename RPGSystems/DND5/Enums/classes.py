from enum import Enum


class Classes(Enum):
	__order__ = "Classes is iterable"

	#race not recognized
	NO_CLASS = -1

	BARBARIAN = 0
	BARD = 1
	CLERIC = 2
	WARRIOR = 3
	ROGUE = 4
	WIZARD = 5

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_CLASS:
			return "unrecognized"
		elif self == self.BARBARIAN:
			return "barbarian"
		elif self == self.BARD:
			return "bard"
		elif self == self.CLERIC:
			return "cleric"
		elif self == self.WARRIOR:
			return "warrior"
		elif self == self.ROGUE:
			return "rogue"
		elif self == self.WIZARD:
			return "wizard"
