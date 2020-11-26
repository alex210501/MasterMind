from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import Screen

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
        button_layout = BoxLayout(orientation="horizontal", padding=(20, 10),
                                    spacing=30, size_hint=(1, 1))
        self.__pseudo_input = TextInput(
            multiline=False, size_hint=(1, .8), pos_hint={'y': 0})
        __button_start = Button(text='MasterMind', size_hint=(0.6, 0.5),
                                pos_hint={'y': 0.4})
        __button_options = Button(text='Options',size_hint=(0.6, 0.5),
                                    pos_hint={'y': 0.4})
        __button_start.bind(on_press=self.switch_to_game)
        __button_options.bind(on_press=self.switch_to_option)
        name_label = Label(text="Borbolla Alejandro", font_size=12, size_hint=(1, .1),
                           halign="right", pos_hint={'x': .42})

        pseudo_layout.add_widget(Label(text="Pseudo : ", size_hint=(1, 1)))
        pseudo_layout.add_widget(self.__pseudo_input)

        button_layout.add_widget(__button_start)
        button_layout.add_widget(__button_options)

        box.add_widget(title)
        box.add_widget(pseudo_layout)
        box.add_widget(self.start_game_type())
        box.add_widget(button_layout)
        box.add_widget(name_label)

        screen.add_widget(box)

        return screen

    def start_game_type(self):
        """
            Build the combobox to choose the game difficulty
        """
        type_game_layout = BoxLayout(orientation="horizontal", padding=(20, 0))

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
