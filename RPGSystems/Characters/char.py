#Standard Python Imports
#

#Internal Imports
from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes
from RPGSystems.Enums.personality import Personality


class Char:
	#base attributes (those who goes in the sheet)
	base_strength = 0
	base_dextrity = 0
	base_constitution = 0
	base_intelligence = 0
	base_windom = 0
	base_charisma = 0

	#modified attributes (+guns and equips)
	strength = 0
	dextrity = 0
	constitution = 0
	intelligence = 0
	windom = 0
	charisma = 0

	#current attributes (temporary, affect by fighting...)
	current_strength = 0
	current_dextrity = 0
	current_constitution = 0
	current_intelligence = 0
	current_windom = 0
	current_charisma = 0

	#proficiency
	proficiency_bonus = 2

	#inspiration
	inspiration = False

	#rance and class
	race = Race.NO_RACE
	rpgclass = Classes.NO_CLASS

	#lvl and ex
	expirience = 0
	level = 1

	#custom characteristics
	age = None
	height = None
	widght = None

	#personalities
	personality = [Personality.NO_PERSONALITY, Personality.NO_PERSONALITY]

	#skills
	skill = {"acrobatics": 0,
			"animal_handling": 0,
			"arcana": 0,
			"athletics": 0,
			"deception": 0,
			"history": 0,
			"insight": 0,
			"intimidation": 0,
			"investigation": 0,
			"medicine": 0,
			"nature": 0,
			"perception": 0,
			"performance": 0,
			"persuasion": 0,
			"religion": 0,
			"sleight_of_hand": 0,
			"stealth": 0,
			"survival": 0}

	def __init__(self):
		pass

	def reset_current_status(self):
		self.current_strength = self.strength
		self.current_dextrity = self.dextrity
		self.current_constitution = self.constitution
		self.current_intelligence = self.intelligence
		self.current_windom = self.windom
		self.current_charisma = self.charisma

	def give_expirience(self, amount):
		self.expirience += amount
		if self.expirience > 300 and self.level < 2:
			self.level = 2
			self.proficiency_bonus += 2
		elif self.expirience > 900 and self.level < 3:
			self.level = 3
			self.proficiency_bonus += 2
		elif self.expirience > 2700 and self.level < 4:
			self.level = 4
			self.proficiency_bonus += 2
		elif self.expirience > 6500 and self.level < 5:
			self.level = 5
			self.proficiency_bonus += 3
		elif self.expirience > 14000 and self.level < 6:
			self.level = 6
			self.proficiency_bonus += 3
		elif self.expirience > 23000 and self.level < 7:
			self.level = 7
			self.proficiency_bonus += 3
		elif self.expirience > 34000 and self.level < 8:
			self.level = 8
			self.proficiency_bonus += 3
		elif self.expirience > 48000 and self.level < 9:
			self.level = 9
			self.proficiency_bonus += 4
		elif self.expirience > 64000 and self.level < 10:
			self.level = 10
			self.proficiency_bonus += 4
		elif self.expirience > 85000 and self.level < 11:
			self.level = 11
			self.proficiency_bonus += 4
		elif self.expirience > 100000 and self.level < 12:
			self.level = 12
			self.proficiency_bonus += 4
		elif self.expirience > 120000 and self.level < 13:
			self.level = 13
			self.proficiency_bonus += 5
		elif self.expirience > 140000 and self.level < 14:
			self.level = 14
			self.proficiency_bonus += 5
		elif self.expirience > 165000 and self.level < 15:
			self.level = 15
			self.proficiency_bonus += 5
		elif self.expirience > 195000 and self.level < 16:
			self.level = 16
			self.proficiency_bonus += 5
		elif self.expirience > 225000 and self.level < 17:
			self.level = 17
			self.proficiency_bonus += 6
		elif self.expirience > 265000 and self.level < 18:
			self.level = 18
			self.proficiency_bonus += 6
		elif self.expirience > 305000 and self.level < 19:
			self.level = 19
			self.proficiency_bonus += 6
		elif self.expirience > 355000 and self.level < 20:
			self.level = 20
			self.proficiency_bonus += 6
