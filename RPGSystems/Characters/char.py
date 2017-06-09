#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes


class Char:
	#base attributes (those who goes in the sheet)
	base_strength = None
	base_dextrity = None
	base_constitution = None
	base_intelligence = None
	base_windom = None
	base_charisma = None

	#modified attributes (+guns and equips)
	strength = None
	dextrity = None
	constitution = None
	intelligence = None
	windom = None
	charisma = None

	#current attributes (temporary, affect by fighting...)
	current_strength = None
	current_dextrity = None
	current_constitution = None
	current_intelligence = None
	current_windom = None
	current_charisma = None

	race = None
	rpgclass = None #class

	def __init__(self):
		self.race = Race.NO_RACE
		self.rpgclass = Classes.NO_CLASSE
	

	def reset_current_status(self):
		self.current_strength = self.strength
		self.current_dextrity = self.dextrity
		self.current_constitution = self.constitution
		self.current_intelligence = self.intelligence
		self.current_windom = self.windom
		self.current_charisma = self.charisma
