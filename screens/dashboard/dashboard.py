import os
import os
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty

class DashboardScreen(Screen):
    username = StringProperty("John")
    rank_name = StringProperty("Bystander")

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(os.path.join(path, 'screens', 'dashboard', 'dashboard.kv'))

    def set_dashboard(self):
        app = App.get_running_app()
        self.username = app.user.username
        self.rank_name = app.user.rank
