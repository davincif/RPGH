#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#Internal Imports
from RPGSystems.DND5.Enums.classes import Classes
from RPGSystems.DND5.Enums.race import Race
from RPGSystems.DND5.Enums.personality import Personality


class CharSheet:
	window = None #the windows to be added on screen by the mainWindow

	header = None #header
	scrolled = None #all the screen

	charNameEntry = None #the entry with the character name
	playerNameEntry = None #the entry with the player name
	level = None #character's level - this field shuld not be editable
	comboPerso = [] #the comboBox of the char's personalites
	Exp = None #the char's Expirience Points

	strengthAdjus = None # \/ SpinButton's Adjustment \/
	dexterityAdjus = None
	constitutionAdjus = None
	intelligenceAdjus = None
	wisdomAdjus = None
	charismaAdjus = None # /\ SpinButton's Adjustment /\

	strengthSPB = None # \/ strength SpinButton \/
	dexteritySPB = None
	constitutionSPB = None
	intelligenceSPB = None
	wisdomSPB = None
	charismaSPB = None # /\ charisma SpinButton /\
	
	def __init__(self, window):
		self.window = window

		self.header = Gtk.HeaderBar(title="RPGHelper")
		self.header.set_subtitle("D&D5 character sheet")
		self.header.props.show_close_button = True
		window.set_titlebar(self.header)
		window.set_resizable(True)
		self.window.set_default_size(100, 700)

		#scrolled panel
		self.scrolled = Gtk.ScrolledWindow()
		self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		#general box
		ggrid = Gtk.Grid()
		ggrid.set_row_spacing(20)
		ggrid.set_column_spacing(20)
		self.scrolled.add_with_viewport(ggrid)

		######HEAD######
		#head
		headGrid = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
		headGrid.set_row_spacing(10)
		headGrid.set_column_spacing(10)

		#char name box
		self.charNameEntry = Gtk.Entry()
		self.charNameEntry.set_text("Char Name")

		#race
		raceBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		comboRace = Gtk.ComboBoxText()
		for i in Classes:
			if i != Classes.NO_CLASS:
				comboRace.append_text(i.get_fancy_name())
		raceBox.pack_start(Gtk.Label("Class"), expand=False, fill=False, padding=0)
		raceBox.pack_start(comboRace, expand=True, fill=True, padding=0)

		#class
		classBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		comboClass = Gtk.ComboBoxText()
		for i in Race:
			if i != Race.NO_RACE and not i.is_uprace():
				comboClass.append_text(i.get_fancy_name())
		classBox.pack_start(Gtk.Label("Race"), expand=False, fill=False, padding=0)
		classBox.pack_start(comboClass, expand=True, fill=True, padding=0)

		#player name box
		charNameBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.playerNameEntry = Gtk.Entry()
		self.playerNameEntry.set_text("Player Name")
		charNameBox.set_valign(Gtk.Align.CENTER)
		charNameBox.pack_start(Gtk.Label("Player Name"), expand=False, fill=False, padding=0)
		charNameBox.pack_start(self.playerNameEntry, expand=True, fill=True, padding=0)

		#Alignment
		AligmentBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		self.comboPerso += [Gtk.ComboBoxText()]
		self.comboPerso += [Gtk.ComboBoxText()]
		for i in Personality:
			if i != Personality.NO_PERSONALITY:
				self.comboPerso[0].append_text(i.get_fancy_name())
				self.comboPerso[1].append_text(i.get_fancy_name())
		AligmentBox.pack_start(Gtk.Label("Alignments"), expand=False, fill=False, padding=0)
		AligmentBox.pack_start(self.comboPerso[0], expand=True, fill=True, padding=0)
		AligmentBox.pack_start(self.comboPerso[1], expand=True, fill=True, padding=0)

		#level
		levelBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.level = Gtk.Entry()
		self.level.set_has_frame(False)
		self.level.set_max_length(2)
		self.level.set_sensitive(False)
		self.level.props.xalign = 0.5
		self.level.set_text("1")
		levelBox.pack_start(Gtk.Label("Level"), expand=False, fill=False, padding=0)
		levelBox.pack_start(self.level, expand=True, fill=True, padding=0)

		#Expirience Points
		expBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.Exp = Gtk.Entry()
		# self.Exp.set_has_frame(False)
		self.Exp.set_text("0")
		expBox.pack_start(Gtk.Label("Expirience"), expand=False, fill=False, padding=0)
		expBox.pack_start(self.Exp, expand=True, fill=True, padding=0)

		headGrid.attach(self.charNameEntry, left=0, top=0, width=2, height=1)
		headGrid.attach(classBox, left=2, top=0, width=1, height=1)
		headGrid.attach(raceBox, left=3, top=0, width=1, height=1)
		headGrid.attach(charNameBox, left=4, top=0, width=3, height=2)
		headGrid.attach(AligmentBox, left=0, top=1, width=2, height=1)
		headGrid.attach(levelBox, left=2, top=1, width=1, height=1)
		headGrid.attach(expBox, left=3, top=1, width=1, height=1)
		######HEAD######

		######ATTRIBUTES######
		#atribute box
		attBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)

		base_spacing = 0
		#strength
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.strengthAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0) #(value, lower, upper, step_increment, page_increment, page_size)
		self.strengthSPB = Gtk.SpinButton()
		self.strengthSPB.set_adjustment(self.strengthAdjus)
		auxBox.pack_start(Gtk.Label("strength"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.strengthSPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)

		#dexterity
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.dexterityAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.dexteritySPB = Gtk.SpinButton()
		self.dexteritySPB.set_adjustment(self.dexterityAdjus)
		auxBox.pack_start(Gtk.Label("dexterity"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.dexteritySPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)

		#constitution
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.constitutionAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.constitutionSPB = Gtk.SpinButton()
		self.constitutionSPB.set_adjustment(self.constitutionAdjus)
		auxBox.pack_start(Gtk.Label("constitution"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.constitutionSPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)

		#intelligence
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.intelligenceAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.intelligenceSPB = Gtk.SpinButton()
		self.intelligenceSPB.set_adjustment(self.intelligenceAdjus)
		auxBox.pack_start(Gtk.Label("intelligence"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.intelligenceSPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)

		#wisdom
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.wisdomAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.wisdomSPB = Gtk.SpinButton()
		self.wisdomSPB.set_adjustment(self.wisdomAdjus)
		auxBox.pack_start(Gtk.Label("wisdom"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.wisdomSPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)

		#charisma
		auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
		self.charismaAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.charismaSPB = Gtk.SpinButton()
		self.charismaSPB.set_adjustment(self.charismaAdjus)
		auxBox.pack_start(Gtk.Label("charisma"), expand=False, fill=False, padding=0)
		auxBox.pack_start(self.charismaSPB, expand=False, fill=False, padding=0)
		attBox.pack_start(auxBox, expand=False, fill=False, padding=0)
		######ATTRIBUTES######

		######INSPIRATION | PROFICIENCY BONUS | SAVING TROWS | SKILLS######
		ipskBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		######INSPIRATION######

		######INSPIRATION######
		######INSPIRATION | PROFICIENCY BONUS | SAVING TROWS | SKILLS######

		#final packing on general box
		ggrid.attach(headGrid, left=0, top=0, width=9, height=1)
		ggrid.attach(attBox, left=0, top=1, width=1, height=6)

		#put all on window and show
		window.set_position(Gtk.WindowPosition.CENTER)
		window.add(self.scrolled)
		window.show_all()
