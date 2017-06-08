#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Internal Imports
#


class MainGameWindow:
	window = None #the windows to be added on screen by the mainWindow
	header = None #header
	
	def __init__(self, window):
		self.window = window

		self.header = Gtk.HeaderBar(title="RPGHelper")
		self.header.set_subtitle("a davincif work, search on github")
		self.header.props.show_close_button = True
		window.set_titlebar(self.header)
		window.set_resizable(True)
		window.set_size_request(window.max_width, window.max_height)
		window.move(0, 0)

		#create the pages
		self.notebook = Gtk.Notebook()
		self.window.add(self.notebook)

		self.page_field = Gtk.Box()
		self.page_field.set_border_width(10)
		self.page_field.add(Gtk.Label("FIELD"))
		self.notebook.append_page(self.page_field, Gtk.Label("Field"))

		self.page_field = Gtk.Box()
		self.page_field.set_border_width(10)
		self.page_field.add(Gtk.Label("SHEETS"))
		self.notebook.append_page(self.page_field, Gtk.Label("Sheets"))

		window.show_all()
