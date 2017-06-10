from enum import Enum
import random


class DiceType(Enum):
	__order__ = "DiceType is iterable"

	COIN = 2
	D4 = 4
	D6 = 6
	D8 = 8
	D10 = 10
	D12 = 12
	D20 = 20

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.COIN:
			return "coin"
		elif self == self.D4:
			return "d4"
		elif self == self.D6:
			return "d6"
		elif self == self.D8:
			return "d8"
		elif self == self.D10:
			return "d10"
		elif self == self.D12:
			return "d12"
		elif self == self.D20:
			return "d20"

	def roll(self):
		return random.randint(1, self.value)

	def is_good_critical(self, value):
		if self.value == value:
			return True
		else:
			return False

	def is_bad_critial(self, value):
		if value == 1 and not self is self.COIN:
			return True
		else:
			return False