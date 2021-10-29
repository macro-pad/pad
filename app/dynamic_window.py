import client
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class DynamicWindow(Gtk.Window):
    first_column_of_row_placed = False
    current_row = 0
    current_column = 0

    def __init__(self):

        super().__init__(title="Grid Example")
        
        self.fullscreen()

        grid = Gtk.Grid()
        grid.__init__(self)

        ui_json = client.get_ui_json()
        rows = ui_json["rows"]
        for key in rows:
            self.add_row(grid, rows[key])
        
        settings_json = ui_json["settings"]
        grid.set_border_width(settings_json["border_width"])
        grid.set_column_spacing(settings_json["column_spacing"])
        grid.set_row_spacing(settings_json["row_spacing"])
       
        self.add(grid)

    def add_row(self, grid, json_row):
        self.first_column_of_row_placed = False
        columns = json_row["columns"]
        for key in columns:
            self.add_column(grid, columns[key], key)
            
        self.current_row += 1
        self.current_column = 0

    def add_column(self, grid, json_column, column_id):
        button = Gtk.Button(label=json_column["name"], expand=True)
        button.connect("clicked", self.test, column_id, 1)

        width = int(json_column["width"])

        grid.attach(button, self.current_column, self.current_row, width, 1)
        self.current_column += width

    def test(self, button, id, value):
        client.post_to_server(id, value)