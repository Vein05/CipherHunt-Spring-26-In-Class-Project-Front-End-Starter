from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty, ColorProperty
from kivy.app import App
from kivy.utils import get_color_from_hex

class TabButton(Button):
    route = StringProperty("dashboard")
    image_filename = StringProperty("house-solid.png")
    is_active = BooleanProperty(False)

    def on_release(self):
        app = App.get_running_app()
        app.shell.change_screen(self.route)


Builder.load_file('custom_widgets.kv')