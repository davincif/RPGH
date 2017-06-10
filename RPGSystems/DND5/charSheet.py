#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#Internal Imports
#


class CharSheet:
	window = None #the windows to be added on screen by the mainWindow
	header = None #header
	
	def __init__(self, window):
		self.window = window

		self.header = Gtk.HeaderBar(title="RPGHelper")
		self.header.set_subtitle("D&D5 character sheet")
		self.header.props.show_close_button = True
		window.set_titlebar(self.header)
		window.set_resizable(True)

		#put all on window and show
		window.set_position(Gtk.WindowPosition.CENTER)
		# window.add()
		window.show_all()
