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
from RPGSystems.DND5.Enums.attribute import Attribute
from RPGSystems.DND5.Enums.skill import Skill
from RPGSystems.DND5.Enums.coin import Coin


class CharSheet:
	window = None #the windows to be added on screen by the mainWindow

	header = None #header
	scrolled = None #all the screen

	charNameEntry = None #the entry with the character name
	playerNameEntry = None #the entry with the player name
	level = None #character's level - this field shuld not be editable
	comboPerso = [] #the comboBox of the char's personalites
	Exp = None #the char's Expirience Points

	attributeAdjus = [] #attributes' spinButton's Adjustment
	attributeSPB = [] #attributes' SpinButton

	insp_checkBox = None #Inspiration CheckBox
	profBonusAdjus = None #Proficiency Bonus Adjustment
	profBonusSPB = None #Proficiency Bonus SpinButton

	stCheckBox = [] #save throw Check Box
	saveTrowEntry = [] #save throw Entry

	skillCheckBox = []
	skillEntry = []
	pwPerception = None #passive wisdom (perception) Entry


	profLang = None #other proficiencies & languages TextView

	armorClass = None #armor class Entry
	initiative = None #initiative Entry
	speed = None #speed Entry
	maxHitPoint = None #maxumim hit points Entry
	curHitPoint = None #current hit points Entry
	tempHitPoints = None #temporary hit points Entry

	DSSCheckBox = [] #death saves successs CheckBox
	DSFCheckBox = [] #death saves failures CheckBox

	atknspells = {} #Name, ATK Bonus and Damage/Type Entry

	coins = {} #coins Entry
	
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
		attBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=25)
		base_spacing = 0
		n = 0
		for at in Attribute:
			if at != Attribute.NO_ATTRIBUTE:
				auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=base_spacing)
				self.attributeAdjus += [Gtk.Adjustment(0, 0, 100, 1, 10, 0)] #(value, lower, upper, step_increment, page_increment, page_size)
				self.attributeSPB += [Gtk.SpinButton()]
				self.attributeSPB[n].set_adjustment(self.attributeAdjus[n])
				auxBox.pack_start(Gtk.Label(at.get_fancy_name()), expand=False, fill=False, padding=0)
				auxBox.pack_start(self.attributeSPB[n], expand=True, fill=True, padding=0)
				attBox.pack_start(auxBox, expand=False, fill=False, padding=0)
				n += 1
		######ATTRIBUTES######

		######INSPIRATION | PROFICIENCY BONUS | SAVING TROWS | SKILLS######
		ipskBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
		######INSPIRATION######
		self.insp_checkBox = Gtk.CheckButton.new_with_label("Inspiration")
		######INSPIRATION######

		######PROFICIENCY BONUS######
		profBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=base_spacing)
		self.profBonusAdjus = Gtk.Adjustment(0, 0, 100, 1, 10, 0)
		self.profBonusSPB = Gtk.SpinButton()
		self.profBonusSPB.set_adjustment(self.profBonusAdjus)
		profBox.pack_start(self.profBonusSPB, expand=False, fill=False, padding=0)
		profBox.pack_start(Gtk.Label("Proficiency Bonus"), expand=False, fill=False, padding=0)
		######PROFICIENCY BONUS######

		######SAVING TROWS######
		stBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		n = 0
		for at in Attribute:
			if at != Attribute.NO_ATTRIBUTE:
				auxBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
				# self.stCheckBox += [Gtk.CheckButton()]
				self.saveTrowEntry += [Gtk.Entry()]
				# auxBox.pack_start(self.stCheckBox[n], expand=False, fill=False, padding=0)
				auxBox.pack_start(self.saveTrowEntry[n], expand=False, fill=False, padding=0)
				auxBox.pack_start(Gtk.Label(at.get_fancy_name()), expand=False, fill=False, padding=0)
				stBox.pack_start(auxBox, expand=False, fill=False, padding=0)
				n += 1
		stBox.pack_start(Gtk.Label("SAVING TROWS"), expand=False, fill=False, padding=0)
		stBox.set_valign(Gtk.Align.CENTER)
		######SAVING TROWS######

		######SKILLS######
		aux2Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		n = 0
		for at in Skill:
			if at != Skill.NO_SKILL:
				auxBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
				self.skillCheckBox += [Gtk.CheckButton()]
				self.skillCheckBox[n].set_sensitive(False)
				self.skillEntry += [Gtk.Entry()]
				auxBox.pack_start(self.skillCheckBox[n], expand=False, fill=False, padding=0)
				auxBox.pack_start(self.skillEntry[n], expand=False, fill=False, padding=0)
				auxBox.pack_start(Gtk.Label(at.get_fancy_name()), expand=False, fill=False, padding=0)
				aux2Box.pack_start(auxBox, expand=False, fill=False, padding=0)
				n += 1
		skillscrolled = Gtk.ScrolledWindow()
		skillscrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		skillscrolled.add_with_viewport(aux2Box)
		skillBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		skillBox.pack_start(skillscrolled, expand=True, fill=True, padding=0)
		skillBox.pack_start(Gtk.Label("SKILLS"), expand=False, fill=False, padding=0)
		skillscrolled.props.min_content_height = 200 #horreble solution, but the only one I found...
		######SKILLS######
		######INSPIRATION | PROFICIENCY BONUS | SAVING TROWS | SKILLS######

		######PASSIVE WISDOM (PERCEPTION)######
		pwBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.pwPerception = Gtk.Entry()
		pwBox.pack_start(self.pwPerception, expand=False, fill=False, padding=0)
		pwBox.pack_start(Gtk.Label("passive wisdom (perception)"), expand=False, fill=False, padding=0)
		######PASSIVE WISDOM (PERCEPTION)######

		######OTHER PROFICIENCIES & LANGUAGES######
		plBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		self.profLang = Gtk.TextView()
		plBox.pack_start(self.profLang, expand=True, fill=True, padding=0)
		plBox.pack_start(Gtk.Label("OTHER PROFICIENCIES & LANGUAGES"), expand=True, fill=True, padding=0)
		######OTHER PROFICIENCIES & LANGUAGES######

		######1º GRAY BOX######
		graybox1 = Gtk.Grid()
		graybox1.set_row_spacing(20)
		graybox1.set_column_spacing(20)

		######ARMOR CLASS######
		armorClassBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		self.armorClass = Gtk.Entry()
		self.armorClass.set_has_frame(False)
		self.armorClass.set_max_length(3)
		self.armorClass.set_sensitive(False)
		self.armorClass.props.xalign = 0.5
		self.armorClass.set_text("0")
		armorClassBox.pack_start(self.armorClass, expand=True, fill=True, padding=0)
		armorClassBox.pack_start(Gtk.Label("armor class"), expand=False, fill=False, padding=0)
		######ARMOR CLASS######

		######INITIATIVE######
		initiativeBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		self.initiative = Gtk.Entry()
		self.initiative.set_has_frame(False)
		self.initiative.set_max_length(3)
		self.initiative.set_sensitive(False)
		self.initiative.props.xalign = 0.5
		self.initiative.set_text("0")
		initiativeBox.pack_start(self.initiative, expand=True, fill=True, padding=0)
		initiativeBox.pack_start(Gtk.Label("initiative"), expand=False, fill=False, padding=0)
		######INITIATIVE######

		######SPEED######
		speedBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		self.speed = Gtk.Entry()
		self.speed.set_has_frame(False)
		self.speed.set_max_length(3)
		self.speed.set_sensitive(False)
		self.speed.props.xalign = 0.5
		self.speed.set_text("0")
		speedBox.pack_start(self.speed, expand=True, fill=True, padding=0)
		speedBox.pack_start(Gtk.Label("speed"), expand=False, fill=False, padding=0)
		######SPEED######

		######CURRENT HIT POINTS######
		pointBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		# pointBox.modify_bg(Gtk.StateType.NORMAL, Gdk.Color(65535, 65535, 65535))
		maxhitpoitBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.maxHitPoint = Gtk.Entry()
		self.maxHitPoint.set_has_frame(False)
		self.maxHitPoint.set_max_length(3)
		self.maxHitPoint.set_sensitive(False)
		self.maxHitPoint.props.xalign = 0.5
		self.maxHitPoint.set_text("0")	
		maxhitpoitBox.pack_start(Gtk.Label("Hit Point Maximum"), expand=False, fill=False, padding=0)
		maxhitpoitBox.pack_start(self.maxHitPoint, expand=True, fill=True, padding=0)
		curHitpoitBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		self.curHitPoint = Gtk.Entry()
		self.curHitPoint.set_has_frame(False)
		self.curHitPoint.set_max_length(3)
		self.curHitPoint.set_sensitive(False)
		self.curHitPoint.props.xalign = 0.5
		self.curHitPoint.set_text("0")	
		curHitpoitBox.pack_start(self.curHitPoint, expand=True, fill=True, padding=0)
		curHitpoitBox.pack_start(Gtk.Label("Current Hit Points"), expand=False, fill=False, padding=0)
		pointBox.pack_start(maxhitpoitBox, expand=True, fill=True, padding=0)
		pointBox.pack_start(curHitpoitBox, expand=True, fill=True, padding=0)
		######CURRENT HIT POINTS######

		######TEMPORARY HIT POINTS######
		tempHitBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		self.tempHitPoints = Gtk.Entry()
		self.tempHitPoints.set_has_frame(False)
		self.tempHitPoints.set_max_length(3)
		self.tempHitPoints.set_sensitive(False)
		self.tempHitPoints.props.xalign = 0.5
		self.tempHitPoints.set_text("0")
		tempHitBox.pack_start(self.tempHitPoints, expand=True, fill=True, padding=0)
		tempHitBox.pack_start(Gtk.Label("Temporary Hit Points"), expand=False, fill=False, padding=0)
		######TEMPORARY HIT POINTS######

		######HIT DICE######
		hitDiceBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
		totalHitDiceBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.totalHitDice = Gtk.Entry()
		self.totalHitDice.set_has_frame(False)
		self.totalHitDice.set_max_length(3)
		self.totalHitDice.set_sensitive(False)
		self.totalHitDice.props.xalign = 0.5
		self.totalHitDice.set_text("0")	
		totalHitDiceBox.pack_start(Gtk.Label("Total Hit Dice"), expand=False, fill=False, padding=0)
		totalHitDiceBox.pack_start(self.totalHitDice, expand=True, fill=True, padding=0)
		curHitDiceBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		self.curHitDice = Gtk.Entry()
		self.curHitDice.set_has_frame(False)
		self.curHitDice.set_max_length(3)
		self.curHitDice.set_sensitive(False)
		self.curHitDice.props.xalign = 0.5
		self.curHitDice.set_text("0")	
		curHitDiceBox.pack_start(self.curHitDice, expand=True, fill=True, padding=0)
		curHitDiceBox.pack_start(Gtk.Label("Hit Dice"), expand=False, fill=False, padding=0)
		hitDiceBox.pack_start(totalHitDiceBox, expand=True, fill=True, padding=0)
		hitDiceBox.pack_start(curHitDiceBox, expand=True, fill=True, padding=0)
		######HIT DICE######

		######DEATH SAVES######
		deathSaveBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

		self.DSSCheckBox += [Gtk.CheckButton(), Gtk.CheckButton(), Gtk.CheckButton()]
		auxBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		auxBox.pack_start(Gtk.Label("successes"), expand=False, fill=False, padding=0)
		for cb in self.DSSCheckBox:
			auxBox.pack_start(cb, expand=True, fill=True, padding=0)
		deathSaveBox.pack_start(auxBox, expand=True, fill=True, padding=0)
		
		auxBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
		self.DSFCheckBox += [Gtk.CheckButton(), Gtk.CheckButton(), Gtk.CheckButton()]
		auxBox.pack_start(Gtk.Label("failures"), expand=False, fill=False, padding=0)
		for cb in self.DSFCheckBox:
			auxBox.pack_start(cb, expand=True, fill=True, padding=0)
		deathSaveBox.pack_start(auxBox, expand=True, fill=True, padding=0)
		deathSaveBox.pack_start(Gtk.Label("Death Saves"), expand=True, fill=True, padding=0)
		######DEATH SAVES######


		graybox1.attach(armorClassBox, left=0, top=0, width=2, height=1)
		graybox1.attach(initiativeBox, left=3, top=0, width=2, height=1)
		graybox1.attach(speedBox, left=5, top=0, width=2, height=1)
		graybox1.attach(pointBox, left=0, top=1, width=6, height=2)
		graybox1.attach(tempHitBox, left=0, top=3, width=6, height=2)
		graybox1.attach(hitDiceBox, left=0, top=5, width=3, height=2)
		graybox1.attach(deathSaveBox, left=3, top=5, width=3, height=2)
		######1º GRAY BOX######

		######ATTACKS & SPELLCASTING######
		#não sei direito como funciona essa parte
		atksplGrid = Gtk.Grid()
		atksplGrid.set_row_spacing(20)
		atksplGrid.set_column_spacing(20)

		self.atknspells = {"Name": Gtk.Entry(),
							"ATK Bonus": Gtk.Entry(),
							"Damage/Type": Gtk.Entry()}
		n = 0
		for k, v in self.atknspells.items():
			auxBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
			auxBox.pack_start(Gtk.Label(k), expand=False, fill=False, padding=0)
			auxBox.pack_start(v, expand=True, fill=True, padding=0)
			if k != "ATK Bonus":
				atksplGrid.attach(auxBox, left=n, top=0, width=2, height=1)
				n += 2
			else:
				atksplGrid.attach(auxBox, left=n, top=0, width=1, height=1)
				n += 1
			atksplGrid.attach(Gtk.Button("+"), left=0, top=1, width=5, height=1)
			atksplGrid.attach(Gtk.Label("ATTACKS & SPELLCASTING"), left=0, top=2, width=5, height=1)
		######ATTACKS & SPELLCASTING######

		######EQUIPMENT######
		equipBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		aux2Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)

		coinsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
		for coin in Coin:
			if coin != Coin.NO_COIN:
				self.coins[coin] = Gtk.Entry()

				auxBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
				auxBox.pack_start(Gtk.Label(coin.get_fancy_name()), expand=True, fill=False, padding=0)
				auxBox.pack_start(self.coins[coin], expand=True, fill=True, padding=0)
				coinsBox.pack_start(auxBox, expand=True, fill=True, padding=0)

		toolsBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
		toolsBox.pack_start(Gtk.Entry(), expand=False, fill=True, padding=0)
		toolsBox.pack_start(Gtk.Button("+"), expand=False, fill=True, padding=0)

		aux2Box.pack_start(coinsBox, expand=True, fill=True, padding=0)
		aux2Box.pack_start(toolsBox, expand=True, fill=True, padding=0)
		equipBox.pack_start(aux2Box, expand=True, fill=True, padding=0)
		equipBox.pack_start(Gtk.Label("EQUIPMENT & BAG"), expand=True, fill=True, padding=0)
		######EQUIPMENT######

		######2º GRAY BOX######
		######2º GRAY BOX######

		######FEATURES & TRAITS######
		######FEATURES & TRAITS######

		#final packing on general box
		ggrid.attach(headGrid, left=0, top=0, width=9, height=1) #head
		ggrid.attach(attBox, left=0, top=1, width=1, height=6) #attributes
		ggrid.attach(self.insp_checkBox, left=1, top=1, width=2, height=1) #inspiration
		ggrid.attach(profBox, left=1, top=2, width=2, height=1) #proficiency bonus
		ggrid.attach(stBox, left=1, top=3, width=2, height=2) #save throws
		ggrid.attach(skillBox, left=1, top=5, width=2, height=2) #skill
		ggrid.attach(pwBox, left=0, top=7, width=3, height=1) #passive wis. (perception)
		ggrid.attach(plBox, left=0, top=8, width=3, height=2) #profic. & languages
		ggrid.attach(graybox1, left=4, top=1, width=3, height=4) #profic. & languages
		ggrid.attach(atksplGrid, left=4, top=5, width=3, height=2) #profic. & languages
		ggrid.attach(equipBox, left=4, top=8, width=3, height=3) #profic. & languages

		#put all on window and show
		window.set_position(Gtk.WindowPosition.CENTER)
		window.add(self.scrolled)
		window.show_all()
