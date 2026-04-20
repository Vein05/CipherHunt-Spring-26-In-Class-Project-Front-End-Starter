from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as hex

class SettingsScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        path = App.get_running_app().base_path
        Builder.load_file(path + "\\screens\\settings\\settings.kv")
