from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.properties import StringProperty, NumericProperty

class DashboardScreen(Screen):
    username = StringProperty("Guest")
    rank = StringProperty("Inquisitor")
    rank_percent_complete = NumericProperty(0)
    rank_points = NumericProperty(45)
    next_rank_points = NumericProperty(100)

    def __init__(self, **kw):
        super().__init__(**kw)
        
        path = App.get_running_app().base_path
        Builder.load_file(path + "\\screens\\dashboard\\dashboard.kv")
        
        self.rank_percent_complete = self.rank_points / self.next_rank_points

    def set_dashboard(self):
        pass
