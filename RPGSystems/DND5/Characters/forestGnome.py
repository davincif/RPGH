#Standard Python Imports
#

#Internal Imports
from RPGSystems.DND5.Enums.race import Race
from RPGSystems.DND5.Enums.classes import Classes
from RPGSystems.DND5.Characters.char import Char
from RPGSystems.DND5.Characters.gnome import Gnome


class ForestGnome(Gnome):
	def __init__(self):
		super()
		self.race = Race.FOREST_GNOME
