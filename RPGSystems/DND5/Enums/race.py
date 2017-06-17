from enum import Enum


class Race(Enum):
	__order__ = "Race is iterable"

	#race not recognized
	NO_RACE = -1

	#elfs
	ELF = 0
	WOOD_ELF = 1
	HIGH_ELF = 2
	BLACK_ELF = 3

	#dwarfs
	DWARF = 50
	HILL_DWARF = 51
	MOUNTAIN_DWARF = 52

	#halflings
	HALFLING = 100
	LIGHT_FEET_HALFLING = 101
	TOUGH_HALFLING = 102

	#half elfs
	HALFELF = 150

	#half Orcs
	HALFORC = 200

	#tiefling
	TIEFLING = 250

	#humans
	HUMAN = 300

	#dragonborns
	DRAGONBORN = 350

	#gnomes
	GNOME = 400
	FOREST_GNOME = 401
	ROCK_GNOME = 402

	#COMMUM METHODS
	def describe(self):
		return self.name, self.value

	def get_fancy_name(self):
		if self == self.NO_RACE:
			return "unrecognized"
		elif self == self.ELF:
			return "elf"
		elif self == self.WOOD_ELF:
			return "wood elf"
		elif self == self.HIGH_ELF:
			return "high elf"
		elif self == self.BLACK_ELF:
			return "black elf"
		elif self == self.DWARF:
			return "dwarf"
		elif self == self.HILL_DWARF:
			return "hill dwarf"
		elif self == self.MOUNTAIN_DWARF:
			return "mountain dwarf"
		elif self == self.HALFLING:
			return "halfling"
		elif self == self.LIGHT_FEET_HALFLING:
			return "light halfling"
		elif self == self.TOUGH_HALFLING:
			return "tough halfling"
		elif self == self.HALFELF:
			return "half-elf"
		elif self == self.HALFORC:
			return "half-orc"
		elif self == self.TIEFLING:
			return "tiefling"
		elif self == self.HUMAN:
			return "human"
		elif self == self.DRAGONBORN:
			return "dragonborn"
		elif self == self.GNOME:
			return "gnome"
		elif self == self.FOREST_GNOME:
			return "forest gnome"
		elif self == self.ROCK_GNOME:
			return "rock gnome"

	def get_uprace(self):
		###
		# return the uprace of the given race
		# or itself if it already is an uprace
		###

		if self == self.NO_RACE:
			return self.NO_RACE
		else:
			return Race(int(self.value / 50)*50)

	def is_uprace(self):
		###
		# return whether a classe is uprace or not, but...
		# ATTETION: a classe can be uprace and subrace at the same type, eg.: humans, halforcs.
		# so, (not is_uprace()) may be differente from (is_subrace())
		###

		if int(self.value / 50)*50 == self.value:
			return True
		else:
			return False

	def is_subrace(self):
		###
		# return whether a classe is subrace or not, but...
		# ATTETION: a classe can be uprace and subrace at the same type, eg.: humans, halforcs.
		# so, (not is_uprace()) may be differente from (is_subrace())
		###

		uprace_value = int(self.value / 50)*50
		if uprace_value != self.value:
			return True
		elif any(uprace_value+1 == item.value for item in Race):
			return False
		else:
			return True

	def comum_name_type(self):
		###
		# return, in a list, what kind of names are commum in that race: for exemple
		# dwarfs have male and female names, while elfs have name for child too.
		###

		typelist = None
		race = self.get_uprace()
		
		if race == Race.ELF:
			typelist = [["child", "male", "female"], ["family", "family translation"]]
		elif race == Race.DWARF:
			typelist = [["male", "female"], ["clan"]]
		elif race == Race.HALFLING:
			typelist = [["male", "female"], ["family"]]
		elif race == Race.HALFELF:
			pass
		elif race == Race.HALFORC:
			typelist = [["male", "female"]]
		elif race == Race.TIEFLING:
			typelist = [["male", "famale"], ["virtue"]]
		elif race == Race.HUMAN:
			typelist = [["male", "female", "surname"], ["calishite", "chondathan",
						"damaran", "illuskan", "mulan", "rashemi","shou", "tethyrian", "turami"]]
		elif race == Race.DRAGONBORN:
			typelist = [["childhood", "male", "famale"], ["clan"]]
		elif race == Race.GNOME:
			typelist = [["male", "female", "nickname"], ["clan"]]

		if typelist is None:
			return []
		else:
			return typelist

	def suggest_name(self, nametype):
		###
		# receive ther race and the disired 'nametype' of sugestion
		# and returns a list with commum names for this race
		# or an empty list if there's anything to suggest for this combination of race and type
		###

		namelist = None
		race = self.get_uprace()

		if race == Race.ELF:
			if nametype == "child":
				namelist = ["Ara", "Bryn", "Del", "Eryn", "Faen", "Innil", "Lael",
							"Mella", "Naill", "Naeris", "Phann", "Rael", "Rinn",
							"Sai", "Syllin", "Thia", "Vall"]
			elif nametype == "male":
				namelist = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro",
							"Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan",
							"Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian",
							"Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen",
							"Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
			elif nametype == "female":
				namelist = ["Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua",
							"Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial",
							"Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele",
							"Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra",
							"Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "X anaphia"]
			elif nametype == "family":
				namelist = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir",
							"Liadon", "Meliamne", "Nailo", "Siannodel", "Xiloscient"]
			elif nametype == "family translation":
				namelist = ["Gemflower", "Starflower", "Moonwhisper", "Diamonddew", "Gemblossom",
							"Silverfrond", "Oakenheel", "Nightbreeze", "Moonbrook", "Goldpetal"]
		elif race == Race.DWARF:
			#suggest names for dwarfs
			if nametype == "male":
				namelist = ["Adrik", "Alberich", "Baer", "Barendd", "Brottor", "Dain",
							"Darrak", "Eberk", "Einkil", "Fargrim", "Gardain", "Harbek",
							"Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
							"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok",
							"Ulfgar", "Veit", "Vondal"]
			elif nametype == "female":
				namelist = ["Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth",
							"Falkrunn", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra",
							"Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl",
							"Torbera", "Torgga", "Vistra"]
			elif nametype == "clan":
				namelist = ["Balderk", "Dankil", "Gorunn", "Holderhek", "Loderr", "Lutgehr",
							"Rumnaheim", "Strakeln", "Torunn", "Ungart"]
		elif race == Race.HALFLING:
			if nametype == "male":
				namelist = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan",
							"Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin",
							"Reed", "Roscoe", "Wellby"]
			elif nametype == "female":
				namelist = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian",
							"Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia",
							"Seraphina", "Shaena", "Trym", "Vani", "Verna"]
			elif nametype == "family":
				namelist = ["Brushgather", "Goodbarrel", "Greenbottle", "High-hill", "Hilltopple",
							"Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
		elif race == Race.HUMAN:
			if nametype == "male calishite":
				namelist = ["Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"]
			elif nametype == "male chondathan" or namelist == "male turami":
				namelist = ["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"]
			elif nametype == "male damaran":
				namelist = ["Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"]
			elif nametype == "male illuskan":
				namelist = ["Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"]
			elif nametype == "male mulan":
				namelist = ["Aoth", "Bareris", "Ehput-Ki", "Kethoth", "Mumed", "Ramas", "So-Kehur", "Thazar-De", "Urhur"]
			elif nametype == "male rashemi":
				namelist = ["Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"]
			elif nametype == "male shou":
				namelist = ["An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"]
			elif nametype == "male tethyrian":
				namelist = ["Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"]

			if nametype == "female calishite":
				namelist = ["Atala", "Ceidil", "Hama", "Jasmal", "Meilil", "Seipora", "Yasheira", "Zasheida"]
			elif nametype == "female chondathan" or namelist == "female turami":
				namelist = ["Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele"]
			elif nametype == "female damaran":
				namelist = ["Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora"]
			elif nametype == "female illuskan":
				namelist = ["Amafrey", "Betha", "Cefrey", "Kethra", "Mara", "Olga", "Silifrey", "Westra"]
			elif nametype == "female mulan":
				namelist = ["Arizima", "Chathi", "Nephis", "Nulara", "Murithi", "Sefris", "Thola", "Umara", "Zolis"]
			elif nametype == "female rashemi":
				namelist = ["Fyevarra", "Hulmarra", "Immith", "Imzel", "Navarra", "Shevarra", "Tammith", "Yuldra"]
			elif nametype == "female shou":
				namelist = ["Bai", "Chao", "Jia", "Lei", "Mei", "Qiao", "Shui", "Tai"]
			elif nametype == "female tethyrian":
				namelist = ["Balama", "Dona", "Faila", "Jalana", "Luisa", "Marta", "Quara", "Selise", "Vonda"]

			if nametype == "surname calishite":
				namelist = [ "Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"]
			elif nametype == "surname chondathan" or namelist == "surname turami":
				namelist = ["Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"]
			elif nametype == "surname damaran":
				namelist = ["Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"]
			elif nametype == "surname illuskan":
				namelist = ["Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"]
			elif nametype == "surname mulan":
				namelist = ["Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"]
			elif nametype == "surname rashemi":
				namelist = ["Chergoba", "Dyernina", "Iltazyara", "Murnyethara", "Stayanoga", "Ulmokina"]
			elif nametype == "surname shou":
				namelist = ["Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"]
			elif nametype == "surname tethyrian":
				namelist = ["Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"]
		elif race == Race.HALFORC:
			if nametype == "male":
				namelist = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk",
				"Mhurren", "Ront", "Shump", "Thokk"]
			elif nametype == "female":
				namelist = ["Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka",
				"Shautha", "Sutha", "Vola", "Volen", "Yevelda"]
		elif race == Race.TIEFLING:
			if nametype == "male":
				namelist = ["Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon",
							"Leucis", "Melech", "Mordai", "Morthos", "Pelaios", "Skamos", "Therai"]
			elif nametype == "female":
				namelist = ["Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista",
							"Lerissa", "Makaria", "Nemeia", "Orianna", "Phelaia", "Rieta"]
			elif nametype == "virtue":
				namelist = ["Art", "Carrion", "Chant", "Creed", "Despair", "Excellence", "Fear",
							"Glory", "Hope", "Ideal", "Music", "Nowhere", "Open", "Poetry", "Quest",
							"Random", "Reverence", "Sorrow", "Temerity", "Torment", "Weary"]
		elif race == Race.HALFELF:
			pass
		elif race == Race.DRAGONBORN:
			if nametype == "male":
				namelist = ["Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv",
							"Medrash", "Mehen", "Nadarr", "Pandjed", "Patrin", "Rhogar", "Shamash",
							"Shedinn", "Tarhun", "Torinn"] 
			elif nametype == "female":
				namelist = ["Akra", "Biri", "Daar", "Farideh", "Harann", "Flavilar", "Jheri", "Kava",
							"Korinn", "Mishann", "Nala", "Perra", "Raiann", "Sora", "Surina",
							"Thava", "Uadjit"]
			elif nametype == "childhood":
				namelist = ["Climber", "Earbender", "Leaper", "Pious", "Shieldbiter", "Zealous"]
			elif nametype == "clan":
				namelist = ["Clethtinthiallor", "Daardendrian", "Delmirev", "Drachedandion",
							"Fenkenkabradon", "Kepeshkmolik", "Kerrhylon", "Kimbatuul",
							"Linxakasendalor", "Myastan", "Nemmonis", "Norixius", "Ophinshtalajiir",
							"Prexijandilin", "Shestendeliath", "Turnuroth", "Verthisathurgiesh",
							"Yarjerit"]
		elif race == Race.GNOME:
			if nametype == "male":
				namelist = ["Alston", "Alvyn", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon",
							"Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo",
							"Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn",
							"Wrenn", "Zook"]
			elif nametype == "female":
				namelist = ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella",
							"Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnab",
							"Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana",
							"Waywocket", "Zanna"]
			elif nametype == "clan":
				namelist = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel",
							"Raulnor", "Scheppen", "Timbers", "Turen"]
			elif nametype == "nickname":
				namelist = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter",
							"Fnipper", "Ku", "Nim", "Oneshoe", "Pock", "Sparklegem", "Stumbleduck"]
		if namelist is None:
			return []
		else:
			return namelist
