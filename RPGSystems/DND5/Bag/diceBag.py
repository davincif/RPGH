#Standard Python Imports
import random

#Internal Imports
from RPGSystems.DND5.Enums.diceType import DiceType

class DiceBag:
	dice = None

	def __init__(self):
		self.dice = []

	def add_dice(self, dice):
		self.dice += [dice]

	def roll(self):
		points = 0

		if self.dice:
			for dado in self.dice:
				points += dado.roll()
		else:
			points = None

		return points
