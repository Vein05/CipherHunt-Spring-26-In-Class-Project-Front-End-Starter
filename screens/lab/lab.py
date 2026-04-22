import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
from kivy.utils import get_color_from_hex as hex

class LabScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        app = App.get_running_app()
        assert app is not None

        self.clue_model = app.clue_model
        path = app.base_path
        Builder.load_file(os.path.join(path, 'screens', 'lab', 'lab.kv'))

