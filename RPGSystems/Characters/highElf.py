#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char
from RPGSystems.Characters.elf import Elf


class HighElf(Elf):
	def __init__(self):
		super()
		self.race = Race.HIGH_ELF
