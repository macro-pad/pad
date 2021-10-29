import dynamic_window
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = dynamic_window.DynamicWindow()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
