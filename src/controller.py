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
        self.__gui.start_switch = self.prepare_new_game

    def enter_game(self):
        self.prepare_new_game()
        self.__game.pseudo = self.__gui.get_pseudo()
        self.__game.create_random_combination()
        self.__gui.set_best_score(*self.__database.get_best_score())

    def prepare_new_game(self):
        self.__game.reset()
        self.__gui.clear_mastermind()

    def check_result(self):
        color_combination = self.__gui.get_combination()
        good_position = self.__game.get_position(color_combination)
        self.__gui.good_position = good_position
        self.__gui.good_color = self.__game.get_color_present(color_combination)
        
        if self.__game.is_game_ended(self.__gui.current_attempt, good_position):
            self.__gui.end_game_popup(self.__game.is_game_won(good_position))
            self.__database.write_score(
                self.__game.pseudo, self.__gui.current_attempt)

if __name__ == "__main__":
    mastermind = Controller()
    mastermind.start()
