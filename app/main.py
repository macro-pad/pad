import client
import dynamic_window
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class Main():

    def __init__(self):
        self.window = dynamic_window.DynamicWindow(client.get_ui_json(), self)
        self.add_css()
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
        Gtk.main()

    def reload_window(self, ui_json):
        self.window = dynamic_window.DynamicWindow(ui_json, self)
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

    def add_css(self):
        css = b"""
            #red { background: red; }
        """

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

Main()