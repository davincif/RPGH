from enum import Enum


class Classes(Enum):
	__order__ = "Classes is iterable"

	#race not recognized
	NO_CLASS = -1

	BARBARIAN = 0
	BARD = 1
	CLERIC = 2
	DRUID = 3
	FIGHTER = 4
	MONK = 5
	PALADIN = 6
	RANGER = 7
	ROGUE = 8
	SORCERER = 19
	WARLOCK = 10
	WIZARD = 11

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
		elif self == self.DRUID:
			return "druid"
		elif self == self.FIGHTER:
			return "fighter"
		elif self == self.MONK:
			return "monk"
		elif self == self.PALADIN:
			return "paladin"
		elif self == self.RANGER:
			return "ranger"
		elif self == self.ROGUE:
			return "rogue"
		elif self == self.SORCERER:
			return "sorcerer"
		elif self == self.WARLOCK:
			return "warlock"
		elif self == self.WIZARD:
			return "wizard"
