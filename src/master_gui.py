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

# Declared Images
back_menu_img = "Pictures/left_arrow.png"
good_position_img = "Pictures/true_icon_green.png"
good_color_img = "Pictures/true_icon_orange.png"
wrong_proposition_img = "Pictures/false_icon.png"
red_cross_img = "Pictures/red_cross.png"
red_circle_img = "Pictures/red_circle.png"
blue_circle_img = "Pictures/blue_circle.png"
yellow_circle_img = "Pictures/yellow_circle.png"
green_circle_img = "Pictures/green_circle.png"
white_circle_img = "Pictures/white_circle.png"
black_circle_img = "Pictures/black_circle.png"
purple_circle_img = "Pictures/purple_circle.png"
orange_circle_img = "Pictures/orange_circle.png"

pseudo_format = "Pseudo : {}"
best_score_format = "Best score : {}({})"
color_list = ["red", "blue", "yellow", "green", "white", "black", "purple", "orange"]
color_image = {"No color": red_cross_img, "red": red_circle_img, "blue": blue_circle_img,
                "yellow": yellow_circle_img,"green": green_circle_img,
                "white": white_circle_img, "black": black_circle_img,
                "purple": purple_circle_img, "orange": orange_circle_img}
winning_text = "You win in {} attemps !"
loser_text = "Game over !"

class MyButton(ButtonBehavior, Image):
    def __init__(self, source, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = source
    
class MasterGui(App):
    def __init__(self):
        super().__init__()
        self.start_switch = None
        self.options_switch = None
        self.game_switch = None
        self.validate_combination = None
        self.prepare_normal_game = None
        self.prepare_super_game = None
        self.__best_pseudo = ""
        self.__best_score = 10
        self.__grid_rows = 10
        self.__grid_columns = 4
        self.__current_attempt = 0
        self.__mastermind_layout = []
        self.__advice_layout = []
        self.__color_spinner = []
        self.__master_boll = []
        self.__advice = []

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

    # def prepare_image(self):
    #     self.left_arrow = Image(source='Pictures/left_arrow.png')

    def build_start(self):
        """
            Build the start screen
        """
        screen = Screen(name="start")
        box = BoxLayout(orientation="vertical")
        title = Label(text="My MasterMind Game",
                      font_size=30, pos_hint={'y': 0.3})
        pseudo_layout = BoxLayout(
            orientation="horizontal", padding=(10, 10, 10, 10), size_hint=(1, 0.2))
        button_layout = BoxLayout(orientation="horizontal", padding=(20, 10), spacing=30)
        self.__pseudo_input = TextInput(multiline=False, size_hint=(1, 1), pos_hint={'y': 0})
        self.__button_start = Button(text='MasterMind', size_hint=(0.6, 0.5), pos_hint={'y': 0.2})
        self.__button_options = Button(text='Options', size_hint=(0.6, 0.5), pos_hint={'y': 0.2})
        self.__button_start.bind(on_press=self.switch_to_game)
        self.__button_options.bind(on_press=self.switch_to_option)
        pseudo_layout.add_widget(Label(text="Pseudo : ", size_hint=(1, 1)))
        pseudo_layout.add_widget(self.__pseudo_input)

        button_layout.add_widget(self.__button_start)
        button_layout.add_widget(self.__button_options)

        box.add_widget(title)
        box.add_widget(pseudo_layout)
        box.add_widget(self.start_game_type())
        box.add_widget(button_layout)
        screen.add_widget(box)

        return screen

    def start_game_type(self):
        type_game_layout = BoxLayout(orientation="horizontal", 
                                    padding=(20, 0), size_hint=(1, .3))

        checkbox_normal = CheckBox(group="type", size_hint=(.1, 1), active=True)
        checkbox_super = CheckBox(group="type", size_hint=(.1, 1))

        label_normal = Label(text="Normal", padding=(0, 10))
        label_super = Label(text="Super", padding=(0, 10))

        type_game_layout.add_widget(checkbox_normal)
        type_game_layout.add_widget(label_normal)
        type_game_layout.add_widget(checkbox_super)
        type_game_layout.add_widget(label_super)

        checkbox_normal.bind(active=self.make_normal_game)
        checkbox_super.bind(active=self.make_super_game)

        return type_game_layout

    def build_options(self):
        """
            Build the options screen
        """
        screen = Screen(name="options")
        box = BoxLayout(orientation="vertical")
        up_layout = BoxLayout(orientation="horizontal", size_hint=(.3, .3))

        title = Label(text="Options",
                      font_size=30, halign="center", pos_hint={'y': 0.3})
        # Button(text="Back", size_hint=(.2, 1))
        back_button = MyButton(source=back_menu_img,
                                size_hint=(.2, 1))
        back_button.bind(on_press=self.switch_to_start)
        # button_layout = BoxLayout(orientation="horizontal")
        # self.__button_start = Button(text='Start')
        # self.__button_options = Button(text='Options')

        up_layout.add_widget(back_button)
        up_layout.add_widget(title)

        box.add_widget(up_layout)

        screen.add_widget(box)
        return screen

    def build_mastermind(self):
        """
            Build the options screen
        """
        screen = Screen(name="mastermind")
        box = BoxLayout(orientation="vertical")
        up_layout = BoxLayout(orientation="horizontal", size_hint=(1, .2))
        
        self.pseudo_output = Label(text="No pseudo entered",
                      font_size=15, pos_hint={'y': 0.1})
        self.best_score_output = Label(text=f"No best score",
                              font_size=15, pos_hint={'y': 0.1})
        back_button = back_button = MyButton(source=back_menu_img,
                                            size_hint=(.2, 1), pos_hint = {'y': 0.1})
        back_button.bind(on_press=self.switch_to_start)

        up_layout.add_widget(back_button)
        up_layout.add_widget(self.pseudo_output)
        up_layout.add_widget(self.best_score_output)

        box.add_widget(up_layout)
        box.add_widget(self.mastermind_middle_layout())
        box.add_widget(self.mastermind_bottom_layout())

        screen.add_widget(box)
        return screen

    def mastermind_middle_layout(self):
        middle_layout = BoxLayout(orientation="horizontal", size_hint=(1, 1))
        combination_layout = BoxLayout(orientation="vertical", size_hint=(1, 1))
        advice_layout = BoxLayout(orientation="vertical", size_hint=(.6, 1))

        self.grid_button = GridLayout(rows=self.__grid_rows, cols=self.__grid_columns)

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
                Spinner(text="No color", values=color_list[:6], size_hint=(.4, 1)))
            bottom_layout.add_widget(self.__color_spinner[column])
            self.__color_spinner[column].bind(text=self.change_boll_color)
        
        #Make the fifth spinner invisible
        self.__color_spinner[-1].disabled = True
        self.__color_spinner[-1].opacity = 0

        validate_button = Button(text="Validate")
        validate_button.bind(on_press=self.validate)
        bottom_layout.add_widget(validate_button)

        return bottom_layout

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
        self.pseudo_output.text = pseudo_format.format(self.get_pseudo())

    def get_pseudo(self):
        if self.__pseudo_input.text == '':
            return "/"
        return self.__pseudo_input.text

    def set_best_score(self, pseudo, score):
        if pseudo != "":
            self.__best_pseudo = str(pseudo)
            self.__best_score = str(score)
            self.best_score_output.text = best_score_format.format(self.__best_pseudo,
                                                                   self.__best_score)

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
    
    def change_boll_color(self, source, color):
        index = self.__color_spinner.index(source)
        
        if index <= (len(self.__master_boll[self.__current_attempt]) - 1):
            self.__master_boll[self.__current_attempt][index].source = color_image[color]

    def validate(self, source):
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
            combination.append(color_list.index(color))

        print(f"Combination tested : {combination}")

        return combination[:]

    def set_advice(self, good_position, good_color):
        wrong_proposition = self.__grid_columns - good_position - good_color
    
        for _ in range(good_position):
            self.__advice_layout[self.__current_attempt].add_widget(Image(source=good_position_img))
        
        for _ in range(good_color):
            self.__advice_layout[self.__current_attempt].add_widget(
                Image(source=good_color_img))
            
        for _ in range(wrong_proposition):
            self.__advice_layout[self.__current_attempt].add_widget(
                Image(source=wrong_proposition_img))


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
                      auto_dismiss=False)

        home_button.bind(on_press=self.switch_to_start)
        play_again_button.bind(on_press=self.switch_to_game)
        
        home_button.bind(on_release=popup.dismiss)
        play_again_button.bind(on_release=popup.dismiss)

        popup.open()

    @property
    def current_attempt(self):
        return self.__current_attempt + 1

    def make_normal_game(self, *value):
        if self.prepare_normal_game is not None:
            self.prepare_normal_game()

        self.__grid_columns = 4
        self.__grid_rows = 10

        # Make the last spinner invisible
        self.__color_spinner[-1].disabled = True
        self.__color_spinner[-1].opacity = 0

        for column in range(self.__grid_columns):
            self.__color_spinner[column].values = color_list[:6]
    
    def make_super_game(self, *value):
        if self.prepare_super_game is not None:
            self.prepare_super_game()
        self.__grid_columns = 5
        self.__grid_rows = 12

        # Make the last spinner visible
        self.__color_spinner[-1].disabled = False
        self.__color_spinner[-1].opacity = 1

        for column in range(self.__grid_columns):
            self.__color_spinner[column].values = color_list

# Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

if __name__ == "__main__":
    master_gui = MasterGui()
    # master_gui.clear_mastermind()
    master_gui.run()
