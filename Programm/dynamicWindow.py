import client
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class DynamicWindow(Gtk.Window):
    def __init__(self):

        super().__init__(title="Grid Example")
        
        self.fullscreen()

        button1 = Gtk.Button(label="Button 1", expand=True)
        button2 = Gtk.Button(label="Button 2", expand=True)
        button3 = Gtk.Button(label="Button 3", expand=True)
        button4 = Gtk.Button(label="Button 4", expand=True)
        button5 = Gtk.Button(label="Button 5", expand=True)
        button6 = Gtk.Button(label="Button 6", expand=True)

        grid = Gtk.Grid()
        grid.__init__(self)
        
        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        
        gtkbox = Gtk.Box(spacing=6)
        gtkbox.add(grid)

        grid.set_hexpand(True)
        grid.set_vexpand(True)
        grid.set_border_width(30)
       
        self.add(gtkbox)