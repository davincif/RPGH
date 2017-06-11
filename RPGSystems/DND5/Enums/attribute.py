from enum import Enum


class Attribute(Enum):
	__order__ = "Classes is iterable"

	#race not recognized
	NO_ATTRIBUTE = -1

	STRENGTH = 0
	DEXTERITY = 1
	CONSTITUTION = 2
	INTELLIGENCE = 3
	WISDOM = 4
	CHARISMA = 5

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_ATTRIBUTE:
			return "unrecognized"
		elif self == self.STRENGTH:
			return "strength"
		elif self == self.DEXTERITY:
			return "dexterity"
		elif self == self.CONSTITUTION:
			return "constitution"
		elif self == self.INTELLIGENCE:
			return "intelligence"
		elif self == self.WISDOM:
			return "wisdom"
		elif self == self.CHARISMA:
			return "charisma"
