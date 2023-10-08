from kivy.uix.screenmanager import NoTransition, Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.tab import MDTabsBase
from .puntosview import PuntosView
from .newtonview import NewtonView
from .newtoncotesview import NewtonCotesView
from .trapezoidview import TrapezoidView
from .differencesview import DifferencesView

class MenuTab(MDFloatLayout, MDTabsBase):
    pass

class MainView(Screen):
    screen_manager: MDScreenManager

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        name_tab = instance_tab.title
        self.screen_manager.transition = NoTransition()
        if name_tab == 'Puntos': self.ids.screen_manager.current = 'estimated_per_points'
        if name_tab == 'Newton-Raphson': self.ids.screen_manager.current = 'newton_raphson'
        if name_tab == 'Diferencias': self.ids.screen_manager.current = 'divided_differences'
        if name_tab == 'Trapecio': self.ids.screen_manager.current = 'composed_trapezoid'
        if name_tab == 'Newton-Cotes': self.ids.screen_manager.current = 'newton_cotes'
