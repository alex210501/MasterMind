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

pseudo_format = "Pseudo : {}"
best_score_format = "Best score : {}({})"
color_list = ["red", "blue", "yellow", "green", "white", "black"]
color_image = {"No color": "Pictures/red_cross.png", "red": 'Pictures/red_circle.png', "blue": 'Pictures/blue_circle.png',
                "yellow": 'Pictures/yellow_circle.png',"green": 'Pictures/green_circle.png',
                "white": 'Pictures/white_circle.png', "black": 'Pictures/black_circle.png'}
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
        self.__best_pseudo = ""
        self.__best_score = 10
        self.__grid_rows = 10
        self.__grid_columns = 4
        self.__current_attempt = 0
        self.__mastermind_layout = []
        self.__color_spinner = []
        self.__good_position = []
        self.__good_color = []
        self.__master_boll = []

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
        box.add_widget(button_layout)
        screen.add_widget(box)

        return screen

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
        back_button = MyButton(source="Pictures/left_arrow.png",
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
        back_button = back_button = MyButton(source="Pictures/left_arrow.png",
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
        left_layout = BoxLayout(orientation="vertical", size_hint=(1, 1))
        good_position_layout = BoxLayout(orientation="vertical", size_hint=(.3, 1))
        good_color_layout = BoxLayout(orientation="vertical", size_hint=(.3, 1))

        self.grid_button = GridLayout(rows=self.__grid_rows, cols=self.__grid_columns)

        left_layout.add_widget(Label(text='Combination'))

        good_position_layout.add_widget(Label(text="Good position"))
        good_color_layout.add_widget(Label(text="Good color"))

        for row in range(self.__grid_rows):
            self.__mastermind_layout.append(BoxLayout(
                                            orientation="horizontal", padding=(0, 5)))
            left_layout.add_widget(self.__mastermind_layout[row])
            self.__good_position.append(Label(text=""))
            self.__good_color.append(Label(text=""))

            good_position_layout.add_widget(self.__good_position[row])
            good_color_layout.add_widget(self.__good_color[row])
        
        middle_layout.add_widget(left_layout)
        middle_layout.add_widget(good_position_layout)
        middle_layout.add_widget(good_color_layout)

        return middle_layout

    def mastermind_bottom_layout(self):
        bottom_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.1))

        for column in range(self.__grid_columns):
            self.__color_spinner.append(Spinner(text="No color", values=color_list, size_hint=(.4, 1)))
            bottom_layout.add_widget(self.__color_spinner[column])
            self.__color_spinner[column].bind(text=self.change_boll_color)
        
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
            self.__good_position[row].text = ""
            self.__good_color[row].text = ""
            self.__master_boll.append([])
        
        # Create master button
        for column in range(self.__grid_columns):
            self.__color_spinner[column].text = "No color"
            self.__master_boll[0].append(
                MyButton(source=color_image['No color']))
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


        self.__current_attempt += 1

        if self.current_attempt < self.__grid_rows - 1:
            for column in range(self.__grid_columns):
                self.__master_boll[self.__current_attempt].append(
                    MyButton(source=color_image['No color']))
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

        end_popup = Popup(title='End game', content=box,
                      size_hint=(None, None), size=(300, 300))

        home_button.bind(on_press=self.switch_to_start)
        play_again_button.bind(on_press=self.switch_to_game)

        # end_popup.bind(on_touch_down=end_popup.dismiss)
        
        end_popup.open()

    @property
    def good_position(self):
        return self.__good_position[self.__current_attempt]

    @good_position.setter
    def good_position(self, position_nb):
        self.__good_position[self.__current_attempt].text = str(position_nb)
    
    @property
    def good_color(self):
        return self.__good_color[self.__current_attempt].text

    @good_color.setter
    def good_color(self, color_nb):
        self.__good_color[self.__current_attempt].text = str(color_nb)

    @property
    def current_attempt(self):
        return self.__current_attempt + 1


# Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

if __name__ == "__main__":
    master_gui = MasterGui()
    # master_gui.clear_mastermind()
    master_gui.run()
