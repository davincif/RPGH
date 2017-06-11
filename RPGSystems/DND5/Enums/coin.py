from enum import Enum


class Coin(Enum):
	__order__ = "Coin is iterable"

	#race not recognized
	NO_COIN = -1

	PLATINUM = 0
	GOLD = 1
	ELECTRUM = 2
	SILVER = 3
	COPPER = 4

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_COIN:
			return "unrecognized"
		elif self == self.PLATINUM:
			return "platinum"
		elif self == self.GOLD:
			return "gold"
		elif self == self.ELECTRUM:
			return "electrum"
		elif self == self.SILVER:
			return "silver"
		elif self == self.COPPER:
			return "copper"
