import client
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
class DynamicWindow(Gtk.Window):
    first_column_of_row_placed = False
    current_row = 0
    current_column = 0
    main = None

    def __init__(self, ui_json, main):
        self.main = main

        super().__init__(title="Macro Pad")

        self.load_ui(ui_json)

    def load_settings(self, grid, ui_json):
        settings_json = ui_json["settings"]
        grid.set_border_width(settings_json["border_width"])
        grid.set_column_spacing(settings_json["column_spacing"])
        grid.set_row_spacing(settings_json["row_spacing"])

    def load_ui(self, ui_json):
        self.fullscreen()
        grid = Gtk.Grid()
        grid.__init__(self)

        self.add_inputs(grid, ui_json)
        self.load_settings(grid, ui_json)

        self.add(grid)

    def add_inputs(self, grid, ui_json):
        rows = ui_json["rows"]
        for key in rows:
            self.add_row(grid, rows[key])

    def add_row(self, grid, json_row):
        self.first_column_of_row_placed = False
        columns = json_row["columns"]
        for key in columns:
            self.add_column(grid, columns[key], key)
            
        self.current_row += 1
        self.current_column = 0

    def add_column(self, grid, json_column, column_id):
        button = None
        if json_column["type"] == "button":
            button = self.add_button(json_column, column_id)

        elif json_column["type"] == "redirect-button":
            button = self.add_redirect_button(json_column, column_id)

        elif json_column["type"] == "slider":
            button = self.add_slider(json_column, column_id)


        width = int(json_column["width"])

        grid.attach(button, self.current_column, self.current_row, width, 1)
        self.current_column += width

    def add_button(self, json_column, column_id):
        button = Gtk.Button(label=json_column["name"], expand=True)
        button.connect("clicked", self.button_clicked, column_id)
        return button

    def add_redirect_button(self, json_column, column_id):
        redirect_button = Gtk.Button(label=json_column["name"], expand=True)
        redirect_button.connect("clicked", self.redirect_button_clicked, column_id)
        return redirect_button

    def add_slider(self, json_column, column_id):
        slider = Gtk.Slider(label=json_column["name"], expand=True)
        slider.connect("clicked", self.slider_slided, column_id)
        return slider

    def button_clicked(self, button, id):
        client.post_to_server(id)

    def redirect_button_clicked(self, button, id):
        self.main.reload_window(client.redirect_to_ui(id))

    def slider_slided(self, slider, id):
        client.post_to_server(id, slider.value)
