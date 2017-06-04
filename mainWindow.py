#Standard Python Imports
import os

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Internal Imports
from winState import WinState
from winInitial import WinInitial

class MainWindow(Gtk.Window):
	#notebook - the notebook to handle the "tabs"
	#page_field - the page which conteins the field of the game
	#page_sheets - the page which conteins the charactes sheet of the game
	#state - the current state of the window

	def __init__(self):
		Gtk.Window.__init__(self, title="RPG Helper")
		self.set_border_width(10)

		self.state = WinState(0).initial_state()
		self.buildWindow()

	def buildWindow(self):
		if self.state == WinState.main_play:
			self.notebook = Gtk.Notebook()
			self.add(self.notebook)

			#Filed page
			self.page_field = Gtk.Box()
			self.page_field.set_border_width(10)
			self.page_field.add(Gtk.Label("FIELD"))
			self.notebook.append_page(self.page_field, Gtk.Label("Field"))

			#Filed page
			self.page_field = Gtk.Box()
			self.page_field.set_border_width(10)
			self.page_field.add(Gtk.Label("SHEETS"))
			self.notebook.append_page(self.page_field, Gtk.Label("Sheets"))
		elif self.state == WinState.choose_game:
			choose_game = WinInitial()
			self.add(choose_game.window)
		else:
			pass
