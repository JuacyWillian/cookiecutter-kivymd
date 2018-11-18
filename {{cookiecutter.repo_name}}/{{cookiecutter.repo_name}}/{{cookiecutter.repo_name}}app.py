from kivy.app import App
from kivymd.theming import ThemeManager


class {{cookiecutter.repo_name | capitalize}}App(App):
    """Basic kivy app

    Edit {{cookiecutter.repo_name}}.kv to get started.
    """
    theme_cls = ThemeManager()
    theme_cls.primary_palette = 'DeepPurple'
    title = {{ cookiecutter.project_name }}

    def build(self):
        return self.root
