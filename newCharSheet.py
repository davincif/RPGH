#Standard Python Imports
import importlib

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#Internal Imports
from Enums.rpgtype import RPGType


class NewCharSheet:
	window = None #the windows to be added on screen by the mainWindow
	header = None #header
	module_name = None #name of the module of the system to be loaded
	module = None #the module to be ran
	
	def __init__(self, window):
		#choose what module to load
		self.module_name = window.rpg_system.get_module() + ".charSheet"
		try:
			self.module = importlib.import_module(self.module_name)
			self.module.CharSheet(window)
		except ImportError:
			print("ERROR:")
			print("\tthe sistem \"" + window.rpg_system.get_fancy_name() + "\" is missing a very importat module")
			print("\tcould not load module \"" + module_name + "\"")
			
			print("\nRPGHelper will try to create a general interface...")

			#try a general interface
			print("\n\nsorry, this is just not implemented yet =/")
		
			self.window = window
			self.header = None #will change

			#put all on window and show
			window.set_position(Gtk.WindowPosition.CENTER)
			# window.add()
			window.show_all()
