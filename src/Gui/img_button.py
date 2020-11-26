from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

"""
    Class for add an Image which act like a button
"""

class ImgButton(ButtonBehavior, Image):
    def __init__(self, source, **kwargs):
        super(ImgButton, self).__init__(**kwargs)
        self.source = source
