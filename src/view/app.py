from kivy.uix.screenmanager import NoTransition
from kivymd.app import MDApp, Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from .mainview import MainView

Builder.load_file('src/template/MainView.kv')
Builder.load_file('src/template/PuntosView.kv')
Builder.load_file('src/template/NewtonView.kv')
Builder.load_file('src/template/DifferencesView.kv')
Builder.load_file('src/template/TrapezoidView.kv')
Builder.load_file('src/template/NewtonCotesView.kv')

class MainApp(MDApp):
    screen_manager = ScreenManager()

    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.accent_palette = 'Amber'
        self.theme_cls.material_style = 'M3'
        self.theme_cls.theme_style = 'Dark'
        main_view = MainView(name='MainView')
        main_view.on_enter()
        self.screen_manager.add_widget(main_view)
        self.screen_manager.transition = NoTransition()
        return self.screen_manager

    def on_start(self):
        Window.size = (500, 800)
        Window.set_title('metodos')
