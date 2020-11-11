import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ButtonWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Button Demo")
		self.set_border_width(10)

		hbox = Gtk.Box(spacing=6)
		self.add(hbox)

		button = Gtk.Button.new_with_label("Hello ppl")
		button.connect("clicked", self.on_click_me_clicked)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("_How are you")
		button.connect("clicked", self.on_click_how_clicked)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("_Close")
		button.connect("clicked", self.on_close_clicked)
		hbox.pack_start(button, True, True, 0)

	def on_click_me_clicked(self, button):
		print('"Hello PPL" button was clicked')
	def on_click_how_clicked(self, button):
		print('"How are you" button was clicked')
	def on_close_clicked(self, button):
		print("Closing application")
		Gtk.main_quit()
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
