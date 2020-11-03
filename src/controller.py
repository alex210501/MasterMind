from master_gui import MasterGui
from database import DataBase
from game import Game


class Controller():
    def __init__(self):
        self.__gui = MasterGui()
        self.__database = DataBase()
        self.__game = Game()

        self.prepare_gui_function()

    def start(self):
        self.__gui.run()

    def prepare_gui_function(self):
        self.__gui.game_switch = self.enter_game
        self.__gui.validate_combination = self.check_result

    def enter_game(self):
        self.__game.pseudo = self.__gui.get_pseudo()
        self.__game.create_random_combination()
        self.__gui.set_best_score(*self.__database.get_best_score())

    def check_result(self):
        color_combination = self.__gui.get_combination()
        self.__gui.good_position = self.__game.get_position(color_combination)
        self.__gui.good_color = self.__game.get_color_present(color_combination)
