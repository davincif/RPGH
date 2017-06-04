#Standard Python Imports
import os
import xml.etree.ElementTree as ET

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

#Internal Imports
from Enums import MsgType
from popUpMsg import PopUpMsg


class WinInitial:
	#window - the windows to be added on screen by the mainWindow
	#self.gAmount - game Amount

	def __init__(self, window):
		self.window = window

		#header
		header = Gtk.HeaderBar(title="RPG Helper")
		header.set_subtitle("choose a game save")
		header.props.show_close_button = True
		window.set_titlebar(header)

		#general box
		gbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

		#scroll window
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		flowbox = Gtk.FlowBox()
		flowbox.set_valign(Gtk.Align.START)
		flowbox.set_max_children_per_line(1)
		flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

		scrolled.add(flowbox)
		flowbox.set_activate_on_single_click(False)

		#get the root in xml
		xmlfile = ET.parse("games/games.xml")
		groot = xmlfile.getroot() #game root

		#check consistency
		advised = False
		games = groot.findall("game")
		for elem in games:
			if not os.path.isdir(elem.find("name").text):
				#game folder don't exist!
				if not advised:
					advised = True
					popup = PopUpMsg(window)
					popup.pop_it_up(title="Game Missing!",
							text="some game folder was erased or moved from the RPGHelper's games folder",
							msgtype=MsgType.ERROR)
				# groot.remove(elem)
		if advised:
			xmlfile.write("games/tt.xml")

		#create one option for eatch game
		games = groot.findall("game")
		for elem in games:
			grid = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
			grid.set_row_spacing(10)
			flowbox.add(grid)

			#game name and last play time
			title = Gtk.Label()
			title.set_markup("<big><b>"+elem.find("./name").text+"</b></big>")
			title.set_line_wrap(True)
			title.set_xalign(0.5)
			
			aux = elem.find("./last_play/day").text + "/" + elem.find("./last_play/month").text
			aux += "/" + elem.find("./last_play/year").text
			aux += " at " + elem.find("./last_play/time").text
			aux = "<i>" + aux + "</i>"
			timedate = Gtk.Label()
			timedate.set_markup(aux)
			timedate.set_xalign(1)
			# timedate.set_line_wrap(True)
			# timedate.set_justify(Gtk.Justification.LEFT)
			# timedate.props.justify = Gtk.Justification.LEFT

			#load and delete bottuns
			loadbutton = Gtk.Button(label="Load")
			delbutton = Gtk.Button(label="Delete")

			#add in the grid
			grid.attach(title, left=0, top=0, width=8, height=1)
			grid.attach(timedate, left=4, top=1, width=4, height=1)
			grid.attach(loadbutton, left=0, top=2, width=1, height=1)
			grid.attach(delbutton, left=7, top=2, width=1, height=1)
			flowbox.add(Gtk.HSeparator())

		#final packing
		gbox.pack_start(scrolled, expand=True, fill=True, padding=0)
		newgame_button = Gtk.Button(label="New Game")
		gbox.pack_start(newgame_button, expand=False, fill=False, padding=0)
		self.window.add(gbox)

		#correctly resizing
		self.gAmount = len(games) #gameAmount
		width = window.gdk_screen.get_width()*0.2
		height = window.gdk_screen.get_height()

		if width > 250:
			width = 250

		if self.gAmount == 0:
			height = 200
		else:
			aux = self.gAmount*110 + 50
			if aux > height*0.8:
				height *= 0.8
			else:
				height = aux

		window.set_default_size(int(width), int(height))
		window.set_resizable(False)
