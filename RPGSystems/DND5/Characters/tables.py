from RPGSystems.DND5.Enums.race import Race


def lvl_for_exp(exp):
	###
	# return the level and prificiency bonus that
	# a character must have based in the given exp
	# or None, None in caso of a out of range argument
	###

	if exp >= 355000:
		return 20, 6
	elif exp >= 305000:
		return 19, 6
	elif exp >= 265000:
		return 18, 6
	elif exp >= 225000:
		return 17, 6
	elif exp >= 195000:
		return 16, 5
	elif exp >= 165000:
		return 15, 5
	elif exp >= 140000:
		return 14, 5
	elif exp >= 120000:
		return 13, 5
	elif exp >= 100000:
		return 12, 4
	elif exp >= 85000:
		return 11, 4
	elif exp >= 64000:
		return 10, 4
	elif exp >= 48000:
		return 9, 4
	elif exp >= 34000:
		return 8, 3
	elif exp >= 23000:
		return 7, 3
	elif exp >= 14000:
		return 6, 3
	elif exp >= 6500:
		return 5, 3
	elif exp >= 2700:
		return 4, 2
	elif exp >= 900:
		return 3, 2
	elif exp >= 300:
		return 2, 2
	elif exp < 300:
		return 1, 2
	elif exp < 0:
		return 0, 0
	else:
		return None, None

def exp_for_level(lvl):
	###
	# return the minumim exp and the prificiency bonus that
	# a character must have based in the given level
	# or None, None in caso of a out of range argument
	###

	if lvl == 1:
		return 0, 2
	elif lvl == 2:
		return 300, 2
	elif lvl == 3:
		return 900, 2
	elif lvl == 4:
		return 2700, 2
	elif lvl == 5:
		return 6500, 3
	elif lvl == 6:
		return 14000, 3
	elif lvl == 7:
		return 23000, 3
	elif lvl == 8:
		return 3400, 3
	elif lvl == 9:
		return 48000, 4
	elif lvl == 10:
		return 64000, 4
	elif lvl == 11:
		return 85000, 4
	elif lvl == 12:
		return 100000, 4
	elif lvl == 13:
		return 120000, 5
	elif lvl == 14:
		return 140000, 5
	elif lvl == 15:
		return 165000, 5
	elif lvl == 16:
		return 195000, 5
	elif lvl == 17:
		return 225000, 6
	elif lvl == 18:
		return 265000, 6
	elif lvl == 19:
		return 305000, 6
	elif lvl == 20:
		return 355000, 6
	else: return None, None

def mod_by_att(att_point):
	###
	# returns the modificator for that atribute
	###
	if att_point <= 30:
		return int(att_point/2) -5
	else:
		return 10

def suggest_name(race, sex):
	###
	# receive ther race and the string "male", "female" or "clan"
	# and returns a list with commum names for this race and sex
	# or an empty list if there's anything to suggest
	###

	namelist = None

	if race.get_uprace == Race.DWARF:
		#suggest names for dwarfs
		if sex == "male":
			namelist = ["Adrik", "Alberich", "Baer", "Barendd", "Brottor", "Dain",
						"Darrak", "Eberk", "Einkil", "Fargrim", "Gardain", "Harbek",
						"Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
						"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok",
						"Ulfgar", "Veit", "Vondal"]
		elif sex == "female":
			namelist = ["Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth",
						"Falkrunn", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra",
						"Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl",
						"Torbera", "Torgga", "Vistra"]
		elif sex == "clan":
			namelist = ["Balderk", "Dankil", "Gorunn", "Holderhek", "Loderr", "Lutgehr",
						"Rumnaheim", "Strakeln", "Torunn", "Ungart"]

	if namelist is None:
		return []
	else:
		return namelist
