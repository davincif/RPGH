#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char
from RPGSystems.Characters.halfling import Halfling


class LightFeetHalfling(Halfling):
	def __init__(self):
		super()
		self.race = Race.LIGHT_FEET_HALFLING
