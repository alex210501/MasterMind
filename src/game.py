import random

class Game:
    def __init__(self):
        self.__pseudo = ""
        self.__max_color = 6
        self.__combination_nb = 4 # Column number
        self.__code = []
    @property
    def pseudo(self):
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo_enter):
        self.__pseudo = pseudo_enter

    def create_random_combination(self):
        self.__code = []

        for _ in range(self.__combination_nb):
            self.__code.append(random.randrange(self.__max_color))
        
        print(f"The secret code is {self.__code}")

        return self.__code
    
    @property
    def code(self):
        return self.__code

    def get_color_present(self, combination):
        color_present = 0

        for color in combination:
            if color in self.__code:
                color_present += 1
        
        return color_present
    
    def get_position(self, combination):
        good_position = 0

        for position, color in enumerate(combination):
            if self.__code[position] == color:
                good_position += 1

        return good_position

if __name__ == "__main__":
    my_game = Game()
    my_game.pseudo = "alex210501"
    print(f'The current pseudo is {my_game.pseudo}')
    my_game.create_random_combination()
