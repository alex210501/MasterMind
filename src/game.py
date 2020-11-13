import random

class Game:
    def __init__(self):
        self.__pseudo = ""
        self.__score = 10
        self.__max_attempt = 10
        self.__max_color = 6
        self.__combination_nb = 4 # Column number
        self.__game_mode = "normal"
        self.__code = []
    
    @property
    def pseudo(self):
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo_enter):
        self.__pseudo = pseudo_enter

    def reset(self):
        self.__pseudo = ""
        self.__code = []

    def create_random_combination(self):
        self.__code = []

        for _ in range(self.__combination_nb):
            current_color = random.randrange(1, self.__max_color)
            while current_color in self.__code:
                current_color = random.randrange(1, self.__max_color)
            self.__code.append(current_color)
        
        print(f"The secret code is {self.__code}")

        return self.__code
    
    @property
    def code(self):
        return self.__code

    def check_combination(self, combination):
        color_present, good_position = 0, 0
        code = self.__code[:]
        combination_copy = combination[:]

        # First, check the position
        for position, color in enumerate(combination):
            if self.__code[position] == color:
                good_position += 1
                combination_copy.remove(color)
                code.remove(color)
        
        # Second, check the color
        for color in combination_copy[:]:
            if color in code:
                combination_copy.remove(color)
                code.remove(color)
                color_present += 1

        return good_position, color_present

    def is_game_ended(self, attempt_nb, good_positions):
        if attempt_nb == self.__max_attempt or good_positions == self.__combination_nb:
            self.__score = self.__max_attempt - attempt_nb
            return True
        return False

    def is_game_won(self, good_positions):
        if good_positions == self.__combination_nb:
            return True
        return False

    def normal_game_rules(self):
        self.__game_mode = "normal"
        self.__max_attempt = 10
        self.__max_color = 6
        self.__combination_nb = 4

    def super_game_rules(self):
        self.__game_mode = "super"
        self.__max_attempt = 12
        self.__max_color = 8
        self.__combination_nb = 5

    @property
    def game_mode(self):
        return self.__game_mode

    @property
    def score(self):
        return self.__score

if __name__ == "__main__":
    my_game = Game()
    my_game.pseudo = "alex210501"
    print(f'The current pseudo is {my_game.pseudo}')
    my_game.create_random_combination()
