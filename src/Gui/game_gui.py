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
from .img_button import ImgButton
from .png import *

pseudo_format = "Pseudo : {}"
best_score_format = "Best score : {}({})"
color_list = ["No color", "red", "blue", "yellow", "green",
              "white", "black", "purple", "orange"]
color_image = {"No color": red_cross_img, "red": red_circle_img, "blue": blue_circle_img,
               "yellow": yellow_circle_img, "green": green_circle_img,
               "white": white_circle_img, "black": black_circle_img,
               "purple": purple_circle_img, "orange": orange_circle_img}

class GameGui:
    def __init__(self):
        self.__blocking_mode = False
        self.__grid_rows = 10
        self.__grid_columns = 4
        self.__best_pseudo = ""
        self.__best_score = 10
        self.__current_attempt = 0
        self.__mastermind_layout = []
        self.__advice_layout = []
        self.__color_spinner = []
        self.__master_boll = []
        self.__advice = []

    def build_mastermind(self):
        """
            Build the options screen
        """
        screen = Screen(name="mastermind")
        box = BoxLayout(orientation="vertical")
        up_layout = BoxLayout(orientation="horizontal", size_hint=(1, .2))

        self.__pseudo_output = Label(text="No pseudo entered",
                                   font_size=15, pos_hint={'y': 0.1})
        self.__best_score_output = Label(text=f"No best score",
                                       font_size=15, pos_hint={'y': 0.1})
        back_button = back_button = ImgButton(source=back_menu_img,
                                             size_hint=(.2, 1), pos_hint={'y': 0.1})
        back_button.bind(on_press=self.switch_to_start)

        up_layout.add_widget(back_button)
        up_layout.add_widget(self.__pseudo_output)
        up_layout.add_widget(self.__best_score_output)

        box.add_widget(up_layout)
        box.add_widget(self.mastermind_middle_layout())
        box.add_widget(self.mastermind_bottom_layout())

        screen.add_widget(box)
        return screen

    def mastermind_middle_layout(self):
        middle_layout = BoxLayout(orientation="horizontal", size_hint=(1, 1))
        combination_layout = BoxLayout(
            orientation="vertical", size_hint=(1, 1))
        advice_layout = BoxLayout(orientation="vertical", size_hint=(.6, 1))

        self.grid_button = GridLayout(
            rows=self.__grid_rows, cols=self.__grid_columns)

        combination_layout.add_widget(Label(text='Combination'))

        advice_layout.add_widget(Label(text="Advice"))

        for row in range(12):
            self.__mastermind_layout.append(BoxLayout(
                                            orientation="horizontal", padding=(0, 5)))
            self.__advice_layout.append(BoxLayout(
                orientation="horizontal", padding=(0, 5)))
            combination_layout.add_widget(self.__mastermind_layout[row])
            advice_layout.add_widget(self.__advice_layout[row])

        middle_layout.add_widget(combination_layout)
        middle_layout.add_widget(advice_layout)

        return middle_layout

    def mastermind_bottom_layout(self):
        bottom_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))

        for column in range(5):
            self.__color_spinner.append(
                Spinner(text="No color", values=color_list[:7], size_hint=(.4, 1)))
            bottom_layout.add_widget(self.__color_spinner[column])
            self.__color_spinner[column].bind(text=self.change_boll_color)

        #Make the fifth spinner invisible
        self.__color_spinner[-1].disabled = True
        self.__color_spinner[-1].opacity = 0

        validate_button = Button(text="Validate")
        validate_button.bind(on_press=self.validate)
        bottom_layout.add_widget(validate_button)

        return bottom_layout

    def clear_mastermind(self):
        self.__master_boll = []

        # Remove all widget and indications
        for row in range(self.__grid_rows):
            self.__mastermind_layout[row].clear_widgets()
            self.__advice_layout[row].clear_widgets()
            self.__master_boll.append([])
        
        # Create master button
        for column in range(self.__grid_columns):
            self.__color_spinner[column].text = "No color"
            self.__master_boll[0].append(
                Image(source=color_image['No color']))
            self.__mastermind_layout[0].add_widget(
                self.__master_boll[0][column])
              
        self.__current_attempt = 0

    def set_best_score(self, pseudo, score):
        if pseudo != "":
            self.__best_pseudo = str(pseudo)
            self.__best_score = str(score)
            self.__best_score_output.text = best_score_format.format(self.__best_pseudo,
                                                                    self.__best_score)

    def set_pseudo(self, pseudo):
        self.__pseudo_output.text = pseudo_format.format(pseudo)

    def change_boll_color(self, source, color):
        if self.__blocking_mode:
            return

        index = self.__color_spinner.index(source)

        if index <= (len(self.__master_boll[self.__current_attempt]) - 1):
            self.__master_boll[self.__current_attempt][index].source = color_image[color]

    def validate(self, source):
        if self.__blocking_mode:
            self.popup_windows("The game is ended ! Restart a new one...")
            return

        if not self.is_boll_completed():
            return

        if self.validate_combination is not None:
            self.validate_combination()

        if self.__current_attempt >= self.__grid_rows - 1:
            return

        self.__current_attempt += 1

        for column in range(self.__grid_columns):
            self.__master_boll[self.__current_attempt].append(
                Image(source=color_image['No color']))
            self.__mastermind_layout[self.__current_attempt].add_widget(
                self.__master_boll[self.__current_attempt][column])
            self.__color_spinner[column].text = "No color"

    def is_boll_completed(self):
        current_boll_list = self.__master_boll[self.__current_attempt]
        for boll in current_boll_list:
            if boll.source == color_image["No color"]:
                self.popup_windows("Complete all the grid !")
                return False
        return True

    def get_combination(self):
        combination = []

        for column in range(self.__grid_columns):
            color = self.__color_spinner[column].text
            combination.append(color)

        print(f"Combination tested : {combination}")

        return combination[:]

    def set_advice(self, good_position, good_color):
        wrong_proposition = self.__grid_columns - good_position - good_color

        for _ in range(good_position):
            self.__advice_layout[self.__current_attempt].add_widget(
                Image(source=good_position_img))

        for _ in range(good_color):
            self.__advice_layout[self.__current_attempt].add_widget(
                Image(source=good_color_img))

        for _ in range(wrong_proposition):
            self.__advice_layout[self.__current_attempt].add_widget(
                Image(source=wrong_proposition_img))

    def normal_game(self):
        self.__grid_columns = 4
        self.__grid_rows = 10

        # Make the last spinner invisible
        self.__color_spinner[-1].disabled = True
        self.__color_spinner[-1].opacity = 0

        for column in range(self.__grid_columns):
            self.__color_spinner[column].values = color_list[:7]
    
    def super_game(self):
        self.__grid_columns = 5
        self.__grid_rows = 12

        # Make the last spinner visible
        self.__color_spinner[-1].disabled = False
        self.__color_spinner[-1].opacity = 1

        for column in range(self.__grid_columns):
            self.__color_spinner[column].values = color_list

    @property
    def current_attempt(self):
        return self.__current_attempt + 1
    
    @property
    def blocking_mode(self):
        return self.__blocking_mode

    @blocking_mode.setter
    def blocking_mode(self, mode):
        self.__blocking_mode = mode
