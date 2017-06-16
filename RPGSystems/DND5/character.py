#Standard Python Imports
#

#Internal Imports
from RPGSystems.DND5.Enums.race import Race
from RPGSystems.DND5.Enums.classes import Classes
from RPGSystems.DND5.Enums.personality import Personality
from RPGSystems.DND5.Enums.diceType import DiceType
from RPGSystems.DND5.Bag.coinBag import CoinBag


class Character:

	#player info (if it is a player)
	is_player = False
	#player_name - only if is player

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

	#saving throw
	save_thow_strength = 0
	save_thow_dextrity = 0
	save_thow_constitution = 0
	save_thow_intelligence = 0
	save_thow_windom = 0
	save_thow_charisma = 0

	#hit points
	life_dice = None
	base_hitpoints = 0
	current_hitpoints = 0

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
	name = None
	age = None
	height = None
	weight = None
	carring_weight = 0

	#personalities
	personality = [Personality.NO_PERSONALITY, Personality.NO_PERSONALITY]

	#money
	coins = CoinBag()

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
