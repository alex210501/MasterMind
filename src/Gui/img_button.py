from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class ImgButton(ButtonBehavior, Image):
    def __init__(self, source, **kwargs):
        super(ImgButton, self).__init__(**kwargs)
        self.source = source
