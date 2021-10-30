import client
import dynamic_window
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Main():

    def __init__(self):
        self.window = dynamic_window.DynamicWindow(client.get_ui_json(), self)
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
        Gtk.main()

    def reload_window(self, ui_json):
        self.window = dynamic_window.DynamicWindow(ui_json, self)
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

Main()