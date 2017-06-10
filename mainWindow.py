#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

#Internal Imports
from Enums import WinState
from winInitial import WinInitial
from mainGameWindow import MainGameWindow
from newCharSheet import NewCharSheet

class MainWindow(Gtk.Window):
	#notebook - the notebook to handle the "tabs"
	#page_field - the page which conteins the field of the game
	#page_sheets - the page which conteins the charactes sheet of the game
	#state - the current state of the window
	#gdk_screen - the Gdk.Screen which holds the screen's settings
	#max_width
	#max_height
	rpg_system = None #the RPG system type being played (settled by winInitial after a game load)

	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_border_width(10)

		#getting windows settings
		self.gdk_screen = Gdk.Screen.get_default()
		self.max_width = self.gdk_screen.get_width()
		self.max_height = self.gdk_screen.get_height()

		self.state = WinState(0).initial_state()
		# self.state = WinState.NEW_CHAR #line for tests
		self.buildWindow()

	def buildWindow(self):
		##
		# Change the window according with the current state
		##

		if self.state == WinState.MAIN_PLAY:
			#clear windows if needed
			self.clear()

			#biuld the correct window
			MainGameWindow(self)

		elif self.state == WinState.CHOOSE_GAME:
			#clear windows if needed
			self.clear()

			#biuld the correct window
			WinInitial(self)
		elif self.state == WinState.NEW_CHAR:
			#clear windows if needed
			self.clear()

			#biuld the correct window
			NewCharSheet(self)
		else:
			pass

	def clear(self):
		##
		# clear all the window's child, if there's any.
		##

		children = self.get_children()
		if children is not None:
			for elem in children:
				if type(elem) == Gtk.Box:
					self.remove(elem)
