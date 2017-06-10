#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#Internal Imports
#


class NewCharSheet:
	window = None #the windows to be added on screen by the mainWindow
	header = None #header
	
	def __init__(self, window):
		self.window = window
		# importlib.import_module()
		print("NEW CHAR SHEET WINDOW")

		#put all on window and show
		window.set_position(Gtk.WindowPosition.CENTER)
		# window.add()
		window.show_all()
