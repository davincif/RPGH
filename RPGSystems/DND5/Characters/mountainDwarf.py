#Standard Python Imports
#

#Internal Imports
from RPGSystems.DND5.Enums.race import Race
from RPGSystems.DND5.Enums.classes import Classes
from RPGSystems.DND5.Characters.char import Char
from RPGSystems.DND5.Characters.dwarf import Dwarf


class MountainDwarf(Dwarf):
	def __init__(self):
		super()
		self.race = Race.MOUNTAIN_DWARF
