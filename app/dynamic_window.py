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
        element = None
        if json_column["type"] == "button":
            element = self.get_button(json_column, column_id)

        elif json_column["type"] == "redirect-button":
            element = self.get_redirect_button(json_column, column_id)

        elif json_column["type"] == "slider":
            element = self.get_scale(json_column, column_id)

        elif json_column["type"] == "json-field":
            element = self.get_json_field(json_column, column_id)

        width = int(json_column["width"])

        grid.attach(element, self.current_column, self.current_row, width, 1)
        self.current_column += width

    def get_button(self, json_column, column_id):
        button = Gtk.Button(label=json_column["name"], expand=True)
        button.connect("clicked", self.button_clicked, column_id)
        button.set_name("button")
        return button

    def get_redirect_button(self, json_column, column_id):
        redirect_button = Gtk.Button(label=json_column["name"], expand=True)
        redirect_button.connect("clicked", self.redirect_button_clicked, column_id)
        redirect_button.set_name("redirect-button")
        return redirect_button

    def get_scale(self, json_column, column_id):
        # scale
        scale = Gtk.Scale().new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        scale.set_value_pos(Gtk.PositionType.BOTTOM)
        scale.set_size_request(24, 128)
        scale.set_tooltip_text(json_column["name"])

        # icon
        icon = Gtk.Image()
        icon.set_tooltip_text(json_column["name"])
        icon.set_from_icon_name("sink.icon_name", Gtk.IconSize.SMALL_TOOLBAR)

        # connect
        scale.connect("value-changed", self.scale_scaled, column_id)

        # style
        scale.set_name("scale")

        return scale

    def get_json_field(self, json_column, column_id):
        dummy_button = Gtk.Button(label=client.get_json_field(column_id, json_column["field_name"]), expand=True)
        dummy_button.set_name("label")
        return dummy_button

    def button_clicked(self, button, id):
        client.post_to_server(id, 1)

    def redirect_button_clicked(self, button, id):
        self.main.reload_window(client.redirect_to_ui(id))

    def scale_scaled(self, scale, id):
        client.post_to_server(id, int(scale.get_value()))
