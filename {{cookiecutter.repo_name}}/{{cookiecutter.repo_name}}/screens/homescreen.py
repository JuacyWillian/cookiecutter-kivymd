from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import *

Builder.load_string("""
#:import MDList kivymd.list.MDList
#:import MDRaisedButton kivymd.button.MDRaisedButton


<HomeScreen>:
    ScrollView:
        do_scroll_x: False

        FloatLayout:
            MDRaisedButton:
                text: 'Hello World KivyMD'
                pos_hint: {'center_x': .5, 'center_y': .5}
    
""")


class HomeScreen(Screen):
    app = ObjectProperty(None)

    def __init__(self, app, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.app = app
