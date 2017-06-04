from enum import Enum

class WinState(Enum):
	CHOOSE_GAME = 0
	MAIN_PLAY = 1

	#OVERWRITE METHODS
	def __str__(self):
		if self.value == self.CHOOSE_GAME:
			back = "Choose Game"
		elif self.value == self.MAIN_PLAY:
			back = "Main Play"
		else:
			back = "Incorret window state value"

		return back

	#COMMUM METHODS
	def stantard_state(self):
		return self.MAIN_PLAY

	def initial_state(self):
		return self.CHOOSE_GAME

	def describe(self):
		return self.name, self.value
