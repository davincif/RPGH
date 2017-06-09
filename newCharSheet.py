#Standard Python Imports
#

#Added Python Libraries
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

#Internal Imports
#


class NewCharSheet:
	window = None #the windows to be added on screen by the mainWindow
	header = None #header
	
	def __init__(self, window):
		self.window = window

		self.header = Gtk.HeaderBar(title="RPGHelper")
		self.header.set_subtitle("New Character Sheet")
		self.header.props.show_close_button = True
		window.set_titlebar(self.header)
		window.set_resizable(True)
		# window.set_size_request(window.max_width, window.max_height)
		window.move(0, 0)

		#all sheet will be in here
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

		#general box
		gbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
		scrolled.add(gbox)

		#how to scale a image
		# pixbuf = GdkPixbuf.Pixbuf.new_from_file("images/D&D5Sheet.png")
		# pixbuf = pixbuf.scale_simple(200, 100, GdkPixbuf.PixbufAlphaMode.BILEVEL)
		# self.charsheet = Gtk.Image()
		# self.charsheet.set_from_pixbuf(pixbuf)
		# cropped_buffer = pixbuf.new_subpixbuf(x,y,width,height)

		#top (char name, level, class...)
		topbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		sheetPixbuf = GdkPixbuf.Pixbuf.new_from_file("images/D&D5Sheet.png")
		sheetImage = Gtk.Image()
		wdh, hgt = 2550, 450
		pixbufaux = sheetPixbuf.new_subpixbuf(0, 0, wdh, hgt)
		pixbufaux = pixbufaux.scale_simple(int(wdh*0.5), int(hgt*0.5), GdkPixbuf.PixbufAlphaMode.BILEVEL)
		sheetImage.set_from_pixbuf(pixbufaux)
		topbox.add(sheetImage)

		#final packing
		gbox.pack_start(topbox, expand=False, fill=True, padding=0)

		#put all on window and show
		window.add(scrolled)
		window.show_all()
