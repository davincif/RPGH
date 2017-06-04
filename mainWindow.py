#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

#Internal Imports
from Enums import WinState
from winInitial import WinInitial

class MainWindow(Gtk.Window):
	#notebook - the notebook to handle the "tabs"
	#page_field - the page which conteins the field of the game
	#page_sheets - the page which conteins the charactes sheet of the game
	#state - the current state of the window
	#gdk_screen - the Gdk.Screen which holds the screen's settings
	#max_width
	#max_height

	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_border_width(10)

		#getting windows settings
		self.gdk_screen = Gdk.Screen.get_default()
		self.max_width = self.gdk_screen.get_width()
		self.max_height = self.gdk_screen.get_height()

		self.state = WinState(0).initial_state()
		self.buildWindow()

	def buildWindow(self):
		if self.state == WinState.MAIN_PLAY:
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
		elif self.state == WinState.CHOOSE_GAME:
			choose_game = WinInitial(self)
		else:
			pass
