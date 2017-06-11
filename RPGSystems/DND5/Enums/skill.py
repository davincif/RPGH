#Standard Python Imports
from enum import Enum

#Internal Imports
from RPGSystems.DND5.Enums.attribute import Attribute


class Skill(Enum):
	__order__ = "Skill is iterable"

	#race not recognized
	NO_SKILL = -1

	ACROBATICS = 0
	ANIMAL_HANDLING = 1
	ARCANA = 2
	ATHLETICS = 3
	DECEPTION = 4
	HISTORY = 5
	INSIGHT = 6
	INTIMIDATION = 7
	INVESTIGATION = 8
	MEDICINE = 9
	NATURE = 10
	PERCEPTION = 11
	PERFORMANCE = 12
	PERSUASION = 13
	RELIGION = 14
	SLEIGHT_OF_HAND = 15
	STEALTH = 16
	SURVIVAL = 17

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_SKILL:
			return "unrecognized"
		elif self == self.ACROBATICS:
			return "acrobatics"
		elif self == self.ANIMAL_HANDLING:
			return "animal handling"
		elif self == self.ARCANA:
			return "arcana"
		elif self == self.ATHLETICS:
			return "athletics"
		elif self == self.DECEPTION:
			return "deception"
		elif self == self.HISTORY:
			return "history"
		elif self == self.INSIGHT:
			return "insight"
		elif self == self.INTIMIDATION:
			return "intimidation"
		elif self == self.INVESTIGATION:
			return "investigation"
		elif self == self.MEDICINE:
			return "medicine"
		elif self == self.NATURE:
			return "nature"
		elif self == self.PERCEPTION:
			return "perception"
		elif self == self.PERFORMANCE:
			return "performance"
		elif self == self.PERSUASION:
			return "persuasion"
		elif self == self.RELIGION:
			return "religion"
		elif self == self.SLEIGHT_OF_HAND:
			return "sleight of hand"
		elif self == self.STEALTH:
			return "stealth"
		elif self == self.SURVIVAL:
			return "survival"

influence = {
			Skill.ACROBATICS.value: Attribute.DEXTERITY,
			Skill.ANIMAL_HANDLING.value: Attribute.WISDOM,
			Skill.ARCANA.value: Attribute.INTELLIGENCE,
			Skill.ATHLETICS.value: Attribute.STRENGTH,
			Skill.DECEPTION.value: Attribute.CHARISMA,
			Skill.HISTORY.value: Attribute.INTELLIGENCE,
			Skill.INSIGHT.value: Attribute.WISDOM,
			Skill.INTIMIDATION.value: Attribute.CHARISMA,
			Skill.INVESTIGATION.value: Attribute.INTELLIGENCE,
			Skill.MEDICINE.value: Attribute.WISDOM,
			Skill.NATURE.value: Attribute.INTELLIGENCE,
			Skill.PERCEPTION.value: Attribute.WISDOM,
			Skill.PERFORMANCE.value: Attribute.CHARISMA,
			Skill.PERSUASION.value: Attribute.CHARISMA,
			Skill.RELIGION.value: Attribute.INTELLIGENCE,
			Skill.SLEIGHT_OF_HAND.value: Attribute.DEXTERITY,
			Skill.STEALTH.value: Attribute.DEXTERITY,
			Skill.SURVIVAL.value: Attribute.WISDOM
		}
