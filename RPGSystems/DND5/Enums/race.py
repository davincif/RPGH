from enum import Enum


class Race(Enum):
	__order__ = "Race is iterable"

	#race not recognized
	NO_RACE = -1

	#elfs
	ELF = 0
	FOREST_ELF = 1
	HIGH_ELF = 2
	BLACK_ELF = 3

	#dwarfs
	DWARF = 50
	HILL_DWARF = 51
	MOUNTAIN_DWARF = 52

	#halflings
	HALFLING = 100
	LIGHT_FEET_HALFLING = 101
	TOUGH_HALFLING = 102

	#half elfs
	HALFELF = 150

	#half Orcs
	HALFORC = 200

	#tiefling
	TIEFLING = 250

	#humans
	HUMAN = 300

	#draconatos
	DRACONATO = 350

	#gnomes
	GNOME = 400
	FOREST_GNOME = 401
	ROCK_GNOME = 402

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_RACE:
			return "unrecognized"
		elif self == self.ELF:
			return "elf"
		elif self == self.FOREST_ELF:
			return "forest elf"
		elif self == self.HIGH_ELF:
			return "high elf"
		elif self == self.BLACK_ELF:
			return "black elf"
		elif self == self.DWARF:
			return "dwarf"
		elif self == self.HILL_DWARF:
			return "hill dwarf"
		elif self == self.MOUNTAIN_DWARF:
			return "mountain dwarf"
		elif self == self.HALFLING:
			return "halfling"
		elif self == self.LIGHT_FEET_HALFLING:
			return "light halfling"
		elif self == self.TOUGH_HALFLING:
			return "tough halfling"
		elif self == self.HALFELF:
			return "half-elf"
		elif self == self.HALFORC:
			return "half-orc"
		elif self == self.TIEFLING:
			return "tiefling"
		elif self == self.HUMANO:
			return "human"
		elif self == self.DRACONATO:
			return "draconato"
		elif self == self.GNOME:
			return "gnome"
		elif self == self.FOREST_GNOME:
			return "forest gnome"
		elif self == self.ROCK_GNOME:
			return "rock gnome"

	def get_uprace(self):
		if self == self.NO_RACE:
			return self.NO_RACE
		else:
			return Race(int(self.value / 50)*50)