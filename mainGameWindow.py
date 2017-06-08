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

		#general box
		gbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

		#create the pages #THIS 'Notebook' PART IS PROVISORY
		notebook = Gtk.Notebook()

		page_field = Gtk.Box()
		page_field.set_border_width(10)
		page_field.add(Gtk.Label("FIELD"))
		notebook.append_page(page_field, Gtk.Label("Field"))

		page_field = Gtk.Box()
		page_field.set_border_width(10)
		page_field.add(Gtk.Label("SHEETS"))
		notebook.append_page(page_field, Gtk.Label("Sheets"))

		#lateral grid
		lgrid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)
		lgrid.set_row_spacing(10)

		#scrolled to the side panel
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

		#side panel vbox
		spvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		scrolled.add_with_viewport(spvbox)

		#tree view
		self.treeview = Gtk.TreeView()
		spvbox.pack_start(self.treeview, expand=True, fill=True, padding=0)

		#new character button
		new_char = Gtk.Button("new character")
		new_char.connect("clicked", self.create_new_char)
		spvbox.pack_start(new_char, expand=False, fill=False, padding=0)

		#packing all window content
		gbox.pack_start(scrolled, expand=True, fill=True, padding=0)
		gbox.pack_start(notebook, expand=True, fill=True, padding=0)

		#put all on window and show
		window.add(gbox)
		window.show_all()

	def create_new_char(self, widget):
		self.window.state = self.window.state.NEW_CHAR
		self.window.buildWindow()
