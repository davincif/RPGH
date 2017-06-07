#Standard Python Imports
import os
import sys
if not (sys.version_info > (3, 0)):
	#wrong python interpreter
	print("PYTHON 3 REQUIRED\nRPGHelper will probably not work")

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Internal Imports
from mainWindow import MainWindow
from Enums import windowState


def main():
	#checking projects integrity
	if not os.path.isdir("games"):
		print("There's no game directory")
		os.makedirs("games")

		#create game file
		gf = open("games/games.xml", "w")
		gf.write('<?xml version="1.0"?>\n<all>\n</all>\n')
		gf.close()

	#creating windows
	mainwin = MainWindow()
	mainwin.connect("delete-event", Gtk.main_quit)
	mainwin.show_all()
	Gtk.main()


if __name__ == '__main__':
	main()
