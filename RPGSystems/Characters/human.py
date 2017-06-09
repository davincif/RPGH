#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char


class Human(Char):
	def __init__(self):
		super()
		self.race = Race.HUMAN
