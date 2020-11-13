from Gui.master_gui import MasterGui
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
        self.__gui.prepare_normal_game = self.__game.normal_game_rules
        self.__gui.prepare_super_game = self.__game.super_game_rules

    def enter_game(self):
        self.prepare_new_game()
        self.__game.pseudo = self.__gui.pseudo
        self.__game.create_random_combination()
        self.__gui.set_best_score(
            *self.__database.get_best_score(self.__game.game_mode))

    def prepare_new_game(self):
        self.__gui.blocking_mode = False
        self.__game.reset()
        self.__gui.clear_mastermind()

    def check_result(self):
        color_combination = self.__gui.get_combination()

        good_position, color_present = self.__game.check_combination(color_combination)
        self.__gui.set_advice(good_position, color_present)

        # Check if the game is ended
        if self.__game.is_game_ended(self.__gui.current_attempt, good_position):
            self.__gui.blocking_mode = True
            self.__gui.end_game_popup(self.__game.is_game_won(good_position))
            self.__database.write_score(self.__game.pseudo,
                                        self.__game.score,
                                        self.__game.game_mode)

if __name__ == "__main__":
    mastermind = Controller()
    mastermind.start()
