from enum import Enum

class WinState(Enum):
	CHOOSE_GAME = 0
	MAIN_PLAY = 1
	NEW_CHAR = 2

	#COMMUM METHODS
	def stantard_state(self):
		return self.MAIN_PLAY

	def initial_state(self):
		return self.CHOOSE_GAME

	def describe(self):
		return self.name, self.value
