from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from .start_gui import StartGui
from .game_gui import GameGui
from .img_button import ImgButton
from .options_gui import OptionsGui
from .png import *

winning_text = "You win in {} attemps !"
loser_text = "Game over !"

    
class MasterGui(App, StartGui, GameGui, OptionsGui):
    def __init__(self):
        App.__init__(self)
        StartGui.__init__(self)
        GameGui.__init__(self)

        self.start_switch = None
        self.options_switch = None
        self.game_switch = None
        self.validate_combination = None
        self.prepare_normal_game = None
        self.prepare_super_game = None

    def build(self):
        """
            Create the screen manager
        """
        self.__manager = ScreenManager()
        self.__manager.add_widget(self.build_start())
        self.__manager.add_widget(self.build_options())
        self.__manager.add_widget(self.build_mastermind())

        self.__manager.current = "start"

        return self.__manager

    def switch_to_option(self, source):
        if self.options_switch is not None:
            self.options_switch()
        
        self.__manager.transition.direction = "left"
        self.__manager.current = "options"

    def switch_to_start(self, source):
        if self.start_switch is not None:
            self.start_switch()

        self.__manager.transition.direction = "right"
        self.__manager.current = "start"

    def switch_to_game(self, source):
        if self.game_switch is not None:
            self.game_switch()

        self.clear_mastermind()
        self.__manager.transition.direction = "left"
        self.__manager.current = "mastermind"
        self.set_pseudo(self.pseudo)

    def popup_windows(self, message):
        box = BoxLayout(orientation="vertical")

        error_message = Label(text=message)
        skip_button = Button(text="Close the windows", size_hint=(1, .2))

        box.add_widget(error_message)
        box.add_widget(skip_button)

        popup = Popup(title='Warning', content=box,
                      size_hint=(None, None), size=(300, 300))

        skip_button.bind(on_press=popup.dismiss)

        popup.open()

    def end_game_popup(self, is_won):
        if is_won:
            text_to_disp = winning_text.format(self.current_attempt)
        else:
            text_to_disp = loser_text
        
        box = BoxLayout(orientation="vertical")
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, .2))
        end_message = Label(text=text_to_disp)
        home_button = Button(text="Home")
        play_again_button = Button(text="Play Again")

        button_layout.add_widget(play_again_button)
        button_layout.add_widget(home_button)

        box.add_widget(end_message)
        box.add_widget(button_layout)

        popup = Popup(title='End game', content=box,
                      size_hint=(None, None), size=(300, 300),
                      auto_dismiss=True)

        home_button.bind(on_press=self.switch_to_start)
        play_again_button.bind(on_press=self.switch_to_game)
        
        home_button.bind(on_release=popup.dismiss)
        play_again_button.bind(on_release=popup.dismiss)

        popup.open()

    def make_normal_game(self, *value):
        if self.prepare_normal_game is not None:
            self.prepare_normal_game()

        self.normal_game()
    
    def make_super_game(self, *value):
        if self.prepare_super_game is not None:
            self.prepare_super_game()

        self.super_game()

# Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

if __name__ == "__main__":
    master_gui = MasterGui()
    # master_gui.clear_mastermind()
    master_gui.run()
