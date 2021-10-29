import client
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class DynamicWindow(Gtk.Window):
    first_column_of_row_placed = False
    previous_first_colum = None
    previous_colum = None

    def __init__(self):

        super().__init__(title="Grid Example")
        
        self.fullscreen()

        grid = Gtk.Grid()
        grid.__init__(self)

        ui_json = client.get_ui_json()
        rows = ui_json["rows"]
        for key in rows:
            self.add_row(grid, rows[key])
        
        grid.set_border_width(30)
       
        self.add(grid)

    def add_row(self, grid, json_row):
        self.first_column_of_row_placed = False
        columns = json_row["columns"]
        for key in columns:
            self.add_column(grid, columns[key])

    def add_column(self, grid, json_column):
        button = Gtk.Button(label=json_column["name"], expand=True)
        width = int(json_column["width"])

        if(self.previous_first_colum == None):
            self.add_first_column(grid, button, width)

        elif(not self.first_column_of_row_placed):
            self.add_first_colum_of_row(grid, button, width)

        else:
            grid.attach_next_to(button, self.previous_colum, Gtk.PositionType.RIGHT, width, 1)

    def add_first_colum_of_row(self, grid, button, width):
        grid.attach_next_to(button, self.previous_first_colum, Gtk.PositionType.BOTTOM, width, 1)
        self.first_column_of_row_placed = True
        self.previous_first_colum = button
        self.previous_colum = button

    def add_first_column(self, grid, button, width):
        grid.attach(button, 1, 0, width, 1)
        self.previous_first_colum = button
        self.first_column_of_row_placed = True
