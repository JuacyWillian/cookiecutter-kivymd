from kivy.app import App
from kivymd.theming import ThemeManager


class KivymdbasicApp(App):
    """Basic kivy app

    Edit kivymdbasic.kv to get started.
    """
    theme_cls = ThemeManager()
    theme_cls.primary_palete = 'Teal'

    def build(self):
        return self.root
