#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char
from RPGSystems.Characters.dwarf import Dwarf


class HillDwarf(Dwarf):
	def __init__(self):
		super()
		self.race = Race.HILL_DWARF
