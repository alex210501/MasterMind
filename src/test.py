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
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox

class MasterGui(App):
    def build(self):
        """
            Create the screen manager
        """
        box = BoxLayout(orientation="vertical")
        
        btn1 = ToggleButton(text='Male', group='sex',)
        btn2 = ToggleButton(text='Female', group='sex', state='down')
        btn3 = ToggleButton(text='Mixed', group='sex')


        checkbox = CheckBox(group="sex")
        checkbox2 = CheckBox(group="sex")

        box.add_widget(btn1)
        box.add_widget(btn2)
        box.add_widget(btn3)
        box.add_widget(checkbox)
        box.add_widget(checkbox2)

        return box

testv = MasterGui()
testv.run()
