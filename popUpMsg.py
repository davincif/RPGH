#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#Internal Imports
from Enums import MsgType


class PopUpMsg(Gtk.Dialog):

	def __init__(self, parent):
		Gtk.Dialog.__init__(self, parent=parent)
		self.set_default_size(300, 80)
		self.set_border_width(8)

	def pop_it_up(self, title, text, msgtype):
		if msgtype == MsgType.INFO:
			self.set_title("INFO")
			self.run()
			self.destroy()	
		elif msgtype == MsgType.ERROR:
			self.set_title("ERROR")
			self.add_button("OK", 0)

			if title is not None:
				label = Gtk.Label()
				label.set_markup("<b>"+title+"</b>")
				label.set_line_wrap(True)
				self.vbox.pack_start(label, True, True, 0)
				label.show()

			if text is not None:
				label = Gtk.Label(text)
				label.set_line_wrap(True)
				label.set_justify(Gtk.Justification.FILL)
				self.vbox.pack_start(label, True, True, 0)
				label.show()

			self.run()
			self.destroy()
		elif msgtype == MsgType.WARNING:
			self.set_title("WARNING")
			self.run()
			self.destroy()
		elif msgtype == MsgType.QUESTION:
			self.set_title("QUESTION")
			self.run()
			self.destroy()
		else:
			pass

		return 0 #must return the clicked button, in the future
