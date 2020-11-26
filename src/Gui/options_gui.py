from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from .img_button import ImgButton
from .png import *

rules_txt = "The Mastermind is a code-breaking game. The objective is to find\n \
            a hidden combination of colors at specific positions."

class OptionsGui:
    def __init__(self):
        pass

    def build_options(self):
        """
            Build the options screen
        """
        screen = Screen(name="options")
        box = BoxLayout(orientation="vertical")
        up_layout = BoxLayout(orientation="horizontal", size_hint=(1, .1))

        title = Label(text="Rules", font_size=30,
                      halign="justify")
        rules = Label(text=rules_txt, font_size=25, size_hint=(1, .3))
        # Button(text="Back", size_hint=(.2, 1))
        back_button = ImgButton(source=back_menu_img,
                                size_hint=(.1, 1))
        back_button.bind(on_press=self.switch_to_start)

        up_layout.add_widget(back_button)
        up_layout.add_widget(title)

        box.add_widget(up_layout)
        box.add_widget(rules)
        box.add_widget(self.build_legend_layout())

        screen.add_widget(box)
        return screen

    def build_legend_layout(self):
        """
            Build all the legend widets
        """
        legend_layout = BoxLayout(orientation="vertical")

        gp_layout = BoxLayout(orientation="horizontal", padding=(10, 20))
        gc_layout = BoxLayout(orientation="horizontal", padding=(10, 20))
        bc_layout = BoxLayout(orientation="horizontal", padding=(10, 20))

        good_position = Image(source=good_position_img)
        good_color = Image(source=good_color_img)
        bad_color = Image(source=wrong_proposition_img)

        good_position_l = Label(text="Good color at the good position")
        good_color_l = Label(text="Good color")
        bad_color_l = Label(text="Color not present")

        gp_layout.add_widget(good_position)
        gp_layout.add_widget(good_position_l)
        gc_layout.add_widget(good_color)
        gc_layout.add_widget(good_color_l)
        bc_layout.add_widget(bad_color)
        bc_layout.add_widget(bad_color_l)

        legend_layout.add_widget(gp_layout)
        legend_layout.add_widget(gc_layout)
        legend_layout.add_widget(bc_layout)

        return legend_layout
