#Standard Python Imports
import os
from datetime import datetime
import xml.etree.ElementTree as ET

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

#Internal Imports
from Enums import MsgType
from popUpMsg import PopUpMsg


class WinInitial:
	#main window
	window = None #the windows to be added on screen by the mainWindow

	#gui
	ngwindow = None #create new game window
	ngw_vbox = None #vertical box of the ngwindow
	ngw_vbox_el = None #ngw_vbox error label
	header = None #header
	flowbox = None #where the games are organized
	scrolled = None #an ScrolledWindow, only can erase child by it

	#data
	gAmount = None #game Amount
	xmlfile = None #the file that contains games direcotory

	def __init__(self, window):
		self.window = window

		#header
		self.header = Gtk.HeaderBar(title="RPG Helper")
		self.header.set_subtitle("choose a game save")
		self.header.props.show_close_button = True
		window.set_titlebar(self.header)

		#general box
		gbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

		#get the root in xml
		self.xmlfile = ET.parse("games/games.xml")
		groot = self.xmlfile.getroot() #game root

		#check consistency
		advised = False
		games = groot.findall("game")
		for elem in games:
			if not os.path.isdir("games/" + elem.find("name").text):
				#game folder don't exist!
				if not advised:
					advised = True
					popup = PopUpMsg(window)
					popup.pop_it_up(title="Game Missing!",
							text="some game folder was erased or moved from the RPGHelper's games folder",
							msgtype=MsgType.ERROR)
				groot.remove(elem)
		if advised:
			self.xmlfile.write("games/games.xml")

		#create the game menu window
		self.refresh_game_menu()

		#final packing
		gbox.pack_start(self.scrolled, expand=True, fill=True, padding=0)
		newgame_button = Gtk.Button(label="New Game")
		newgame_button.connect("clicked", self.create_new_game)
		gbox.pack_start(newgame_button, expand=False, fill=False, padding=0)
		window.add(gbox)

		#final window configuration
		window.set_resizable(False)

	def create_new_game(self, widget):
		###
		# open a new window with the information
		# to the user choose the configurations
		###

		#setting window
		self.ngwindow = Gtk.Window(title="Create New Game")
		self.ngwindow.set_attached_to(self.window)
		self.ngwindow.set_modal(True)
		self.ngwindow.set_resizable(False)

		#the window content
		self.ngw_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
		self.ngwindow.add(self.ngw_vbox)

		#input
		self.game_name = Gtk.Entry()
		self.game_name.set_text("My Game")
		self.ngw_vbox.add(self.game_name)

		#ok / cancel buttons
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		hbox.set_halign(Gtk.Align.CENTER)

		ok_button = Gtk.Button(label="OK", stock=Gtk.STOCK_OK)
		ok_button.connect("clicked", self.set_new_game)
		hbox.add(ok_button)
		
		cancel_button = Gtk.Button(stock=Gtk.STOCK_CANCEL)
		cancel_button.connect("clicked", self.cancel_callback)
		hbox.add(cancel_button)

		self.ngw_vbox.add(hbox)

		#show
		self.ngwindow.show_all()

	def cancel_callback(self, widget):
		###
		# do what have to be done to close the new game window
		###

		#destroy the window
		self.ngwindow.destroy()
		self.ngwindow = None

		#update the game menu window
		self.refresh_game_menu()

	def refresh_game_menu(self):
		###
		# it creats or refreshs the piece of the window
		# that hold the existent games do be loaded or deleted
		###

		#erase possible old content
		if self.scrolled is None:
			self.scrolled = Gtk.ScrolledWindow()
			self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		else:
			self.scrolled.remove(self.scrolled.get_child())

		#the box to hold all game options
		if self.flowbox is not None:
			self.flowbox.destroy()
		self.flowbox = Gtk.FlowBox() #it'll be add to a ScrolledWindow later
		self.flowbox.set_valign(Gtk.Align.START)
		self.flowbox.set_max_children_per_line(1)
		self.flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
		self.flowbox.set_activate_on_single_click(False)

		self.scrolled.add_with_viewport(self.flowbox)

		#create one option for eatch game
		games = self.xmlfile.getroot().findall("game")
		for elem in games:
			grid = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
			grid.set_row_spacing(10)
			self.flowbox.add(grid)

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

			#load and delete bottuns
			loadbutton = Gtk.Button(label="Load")
			delbutton = Gtk.Button(label="Delete")
			delbutton.connect("clicked", self.delete_game, elem.find("./name"))

			#add in the grid
			grid.attach(title, left=0, top=0, width=8, height=1)
			grid.attach(timedate, left=4, top=1, width=4, height=1)
			grid.attach(loadbutton, left=0, top=2, width=1, height=1)
			grid.attach(delbutton, left=7, top=2, width=1, height=1)
			self.flowbox.add(Gtk.HSeparator())

		#correctly resizing
		self.gAmount = len(games) #gameAmount
		width = self.window.gdk_screen.get_width()*0.2
		height = self.window.gdk_screen.get_height()*0.8

		if width > 350:
			width = 350

		if self.gAmount == 0:
			height = 130
		else:
			aux = self.gAmount*110 + 130
			if aux < height:
				height = aux

		self.window.set_size_request(int(width), int(height))

		#tells Gtk to redraw
		self.scrolled.show_all()

	#BACK END FUNCTIONS
	def set_new_game(self, widget):
		###
		# it sets everything so to a new game may begin
		###

		path = self.game_name.get_text()
		if os.path.isdir("games/" + path):
			#name already in use, show error
			print("'" + path + "' game already exit")

			if self.ngw_vbox_el is None:
				self.ngw_vbox_el = Gtk.Label()
				aux = "This game already exist"
				aux = "<span background='#ff4d4d'>" + aux + "</span>"
				self.ngw_vbox_el.set_markup(aux)
				self.ngw_vbox.add(self.ngw_vbox_el)

			self.ngw_vbox_el.props.visible = True
		else:
			#create the game's directory
			os.makedirs("games/" + path)

			now = datetime.now()
			time = str(now.hour) + ":" + str(now.minute)
			aux = "<game>\n\t\t<name>{0}</name>\n\t\t<last_play>\n\t\t\t<day>{1}</day>\n\t\t\t<month>{2}</month>\n\t\t\t<year>{3}</year>\n\t\t\t<time>{4}</time>\n\t</last_play>\n</game>\n"
			aux = aux.format(path, now.day, now.month, now.year, time)
			new_element = ET.fromstring(aux)
			root = self.xmlfile.getroot()
			root.append(new_element)
			self.xmlfile.write("games/games.xml")

			#destroy the dialog
			self.cancel_callback(widget)

	def delete_game(self, widget, game_name):
		###
		# do what's needed to delete the game in the path 'game_name'
		# and then remove its folder and entry inthe xml file
		###

		#remove from xml file
		groot = self.xmlfile.getroot()
		games = groot.findall("game")
		for elem in games:
			if elem.find("name") == game_name:
				#missing a confirmation popUp
				groot.remove(elem)
				self.xmlfile.write("games/games.xml")
				break

		#remove the directory
		## Delete everything reachable from the directory named in "top",
		## assuming there are no symbolic links.
		## CAUTION:  This is dangerous!  For example, if top == '/', it
		## could delete all your disk files.
		for root, dirs, files in os.walk("games/" + game_name.text, topdown=False):
			for name in files:
				os.remove(root + name)
			for name in dirs:
				os.rmdir(root + name)
		os.rmdir("games/" + game_name.text)

		#update the game menu window
		self.refresh_game_menu()
