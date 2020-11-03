""" 
    Borbolla Alejandro --- 23-10-2020
    Q1 Labo 4
"""

from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

button_order = ['1', '2', '3', '+', '4', '5', '6', '-', '7',
                '8', '9', '*', '.', '0', '<<', '/']


class GridTest(App):
    def __init__(self):
        super().__init__()
        self.grid_row = 10
        self.grid_column = 4
        self.box_grid = []
        self.current_row = 0

    def build(self):
        self.box = BoxLayout(orientation='vertical')
        bottom_line = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        button = Button(text="Add")
        button.bind(on_press=self.add_grid)
        bottom_line.add_widget(button)
        for number in range(self.grid_row):
            self.box_grid.append(BoxLayout(orientation='horizontal'))
            self.box.add_widget(self.box_grid[number])
        
        self.grid = GridLayout(rows=self.grid_row, cols=self.grid_column)
        self.box.add_widget(self.grid)
        self.box.add_widget(bottom_line)
        # button_grid = GridLayout(rows=5, cols=4)
        # equal_line = BoxLayout(orientation='vertical', size_hint=(1, .3))
        # self.__output = Label()
        # first_line.add_widget(self.__output)
        # self.box.add_widget(first_line)
        # for button_item in button_order:
        #     button = Button(text=button_item)
        #     button_grid.add_widget(button)
        #     button.bind(on_press=self._compute)
        # equal_button = Button(text='=')
        # equal_line.add_widget(equal_button)
        # equal_button.bind(on_press=self._compute)
        # self.box.add_widget(button_grid)
        # self.box.add_widget(equal_line)
        return self.box

    def add_grid(self, source):
        source.background_color = (255,0,0, 25)
        for number in range(self.grid_column):
            button = Button(text=str(number), size_hint=(1, 1))
            self.box_grid[self.current_row].add_widget(button)
        self.current_row += 1

    def _output_operator(self, item, text):
        if item == '.':
            if '.' not in text:
                return text + '.'
        elif item == '<<':
            if text == 'Syntax Error':
                return ''
            return text[:-1]
        elif item == '=':
            try:
                return str(eval(text))
            except:
                return "Syntax Error"
        else:
            return text + item


calculator = GridTest()
calculator.run()
