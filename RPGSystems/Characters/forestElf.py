#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char
from RPGSystems.Characters.elf import Elf


class ForestElf(Elf):
	def __init__(self):
		super()
		self.race = Race.FOREST_ELF
