from enum import Enum

class WinState(Enum):
	choose_game = 0
	main_play = 1

	#OVERWRITE METHODS
	def __str__(self):
		if self.value == 0:
			back = "Choose Game"
		elif self.value == 1:
			back = "Main Play"
		else:
			back = "Incorret state value"

		return back

	#COMMUM METHODS
	def stantard_state(self):
		return self.main_play

	def initial_state(self):
		return self.choose_game

	def describe(self):
		return self.name, self.value
