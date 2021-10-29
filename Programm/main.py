import ApiCalls
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Open")
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("_Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        ApiCalls.open_url("myurl")

    def on_open_clicked(self, button):
        ApiCalls.open_url("myurl")

    def on_close_clicked(self, button):
        Gtk.main_quit()

window = ButtonWindow()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
