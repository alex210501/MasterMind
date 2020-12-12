from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import Screen
from .img_button import ImgButton
from .img import *

class StartGui():
    def __init__(self):
        self.__pseudo = "/"

    def build_start(self):
        """
            Build the start screen
        """
        screen = Screen(name="start")
        box = BoxLayout(orientation="vertical")
        title = Label(text="My MasterMind Game",
                      font_size=30, pos_hint={'y': 0.3})
        pseudo_layout = BoxLayout(orientation="horizontal", padding=(10, 10, 10, 10),
                                    size_hint=(1, 0.3))
        self.__pseudo_input = TextInput(multiline=False, size_hint=(1, .8))
        name_label = Label(text="Borbolla Alejandro", font_size=12, size_hint=(1, .1),
                           halign="right", pos_hint={'x': .42})

        pseudo_layout.add_widget(Label(text="Pseudo : ", size_hint=(1, 1)))
        pseudo_layout.add_widget(self.__pseudo_input)


        box.add_widget(title)
        box.add_widget(pseudo_layout)
        box.add_widget(self.start_game_type())
        box.add_widget(self.menu_layout())
        box.add_widget(name_label)

        screen.add_widget(box)

        return screen

    def menu_layout(self):
        change_menu_layout = BoxLayout(orientation="vertical", padding=(20, 10),
                                       spacing=30, size_hint=(1, 1))
        label_layout = BoxLayout(orientation="horizontal", padding=(20, 10),
                                    spacing=30, size_hint=(1, 0.4))
        button_layout = BoxLayout(orientation="horizontal", padding=(20, 10),
                                    spacing=30, size_hint=(1, 1))

        play_label = Label(text="Play", font_size=20, size_hint=(0.6, 1))
        setting_label = Label(text="Setting", font_size=20, size_hint=(0.6, 1))

        button_start = ImgButton(source=start_img, size_hint=(0.6, 1),
                                pos_hint={'y': 0.4})
        button_options = ImgButton(source=setting_img, size_hint=(0.6, 1),
                                    pos_hint={'y': 0.4})
        button_start.bind(on_press=self.switch_to_game)
        button_options.bind(on_press=self.switch_to_option)

        label_layout.add_widget(play_label)
        label_layout.add_widget(setting_label)
        button_layout.add_widget(button_start)
        button_layout.add_widget(button_options)

        change_menu_layout.add_widget(label_layout)
        change_menu_layout.add_widget(button_layout)

        return change_menu_layout

    def start_game_type(self):
        """
            Build the combobox to choose the game difficulty
        """
        type_game_layout = BoxLayout(orientation="horizontal",
                                    padding=(20, 0), size_hint=(1, .7))

        checkbox_easy = CheckBox(group="type", size_hint=(.1, 1))
        checkbox_normal = CheckBox(group="type", size_hint=(.1, 1),
                                    active=True)
        checkbox_super = CheckBox(group="type", size_hint=(.1, 1))

        label_easy = Label(text="Easy", padding=(0, 10), pos_hint={'y': 0})
        label_normal = Label(text="Normal", padding=(0, 10), pos_hint={'y': 0})
        label_super = Label(text="Super", padding=(0, 10), pos_hint={'y': 0})

        type_game_layout.add_widget(checkbox_easy)
        type_game_layout.add_widget(label_easy)
        type_game_layout.add_widget(checkbox_normal)
        type_game_layout.add_widget(label_normal)
        type_game_layout.add_widget(checkbox_super)
        type_game_layout.add_widget(label_super)

        checkbox_easy.bind(active=self.make_easy_game)
        checkbox_normal.bind(active=self.make_normal_game)
        checkbox_super.bind(active=self.make_super_game)

        return type_game_layout

    @property
    def pseudo(self):
        """
            Accessor for the current score entered
            Return
            -------
            The current pseudo
        """
        if self.__pseudo_input.text == '':
            return "/"
        return self.__pseudo_input.text
