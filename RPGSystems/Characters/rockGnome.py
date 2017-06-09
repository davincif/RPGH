#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Characters.char import Char
from RPGSystems.Characters.gnome import Gnome


class RockGnome(Gnome):
	def __init__(self):
		super()
		self.race = Race.ROCK_GNOME
