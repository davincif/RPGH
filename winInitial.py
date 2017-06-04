#Standard Python Imports
import xml.etree.ElementTree as ET

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WinInitial:
	#window - the windows to be added on screen by the mainWindow

	def __init__(self):
		#creating the listbox
		listbox = Gtk.ListBox()
		# listbox.set_selection_mode(Gtk.SelectionMode.BROWSE)
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		listbox.set_activate_on_single_click(False)

		#get the root in xml
		xmlfile = ET.parse("games/games.xml")
		games = xmlfile.getroot().findall("./")

		#create one option for eatch game
		for elem in games:
			grid = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
			grid.set_row_spacing(10)
			listbox.add(grid)

			#game name and last play time
			title = Gtk.Label(elem.find("./name").text)
			timedate = Gtk.Label("Last play time at " + elem.find("./last_play/time").text
					+ " on " + elem.find("./last_play/day").text + "/" + elem.find("./last_play/month").text
					+ "/" + elem.find("./last_play/year").text)

			#load and delete bottuns
			loadbutton = Gtk.Button(label="Load")
			delbutton = Gtk.Button(label="Delete")

			grid.attach(title, left=0, top=0, width=4, height=1)
			grid.attach(timedate, left=0, top=1, width=2, height=1)
			grid.attach(Gtk.HSeparator(), left=0, top=2, width=4, height=1)
			grid.attach(loadbutton, left=2, top=3, width=1, height=1)
			grid.attach(delbutton, left=3, top=3, width=1, height=1)

		self.window = listbox