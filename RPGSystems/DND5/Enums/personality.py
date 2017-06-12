from enum import Enum


class Personality(Enum):
	__order__ = "Personality is iterable"

	#race not recognized
	NO_PERSONALITY = -1

	GOOD = 0
	BAD = 1
	NEUTRAL = 2
	CAOTIC = 3
	LOYAL = 4

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_PERSONALITY:
			return "unrecognized"
		elif self == self.GOOD:
			return "good"
		elif self == self.BAD:
			return "bad"
		elif self == self.NEUTRAL:
			return "neutral"
		elif self == self.CAOTIC:
			return "caotic"
		elif self == self.LOYAL:
			return "loyal"

	def is_morality(self):
		if self.value <= self.NEUTRAL.value and self.value >= 0:
			return True
		else:
			return False

	def is_law(self):
		if self.value >= self.NEUTRAL.value:
			return True
		else:
			return False
