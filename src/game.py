import random


color_list = ["No color", "red", "blue", "yellow", "green",
              "white", "black", "purple", "orange"]

class Game:
    def __init__(self):
        self.__pseudo = ""
        self.__score = 10
        self.__max_attempt = 10
        self.__max_color = 6
        self.__combination_nb = 4 # Column number
        self.__game_mode = "normal"
        self.__code = []
        self.__game_path = []
    
    @property
    def pseudo(self):
        """
            Accessor for the current pseudo
            Return
            -------
            The current pseudo
        """
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo_enter):
        """
            Setter for the current pseudo
        """
        self.__pseudo = pseudo_enter

    def reset(self):
        """
            Reset all the current data's to start a new game
        """
        self.__pseudo = ""
        self.__code = []
        self.__game_path = []

    def create_random_combination(self):
        """
            Create the random secret code
            Return
            -------
            The secret code
        """
        self.__code = []

        for _ in range(self.__combination_nb):
            index_color = random.randrange(1, self.__max_color + 1)
            if self.__game_mode == "easy":
                while color_list[index_color] in self.__code:
                    index_color = random.randrange(1, self.__max_color + 1)
            self.__code.append(color_list[index_color])
        
        print(f"The secret code is {self.__code}")

        return self.__code
    
    @property
    def code(self):
        """
            Accessor for the secret code
            Return
            -------
            The secret code
        """
        return self.__code

    def check_combination(self, combination):
        """
            Check if the proposed combination is the same as the code
            Parameters
            ----------
            combination : list
                The proposed combination
            Return
            -------
            The good positions, the good colors presents
        """
        color_present, good_position = 0, 0
        self.__game_path.append(combination[:])
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
        """
            Check if the game is ended
            Parameters
            ----------
            attempt_nb : int
                The current attempt number
            good_positions : int
                The color at the good positions presents in the combination
            Return
            -------
            True if the game is ended, False otherwise
        """
        if attempt_nb == self.__max_attempt or good_positions == self.__combination_nb:
            self.__score = self.__max_attempt - attempt_nb
            return True
        return False

    def is_game_won(self, good_positions):
        """
            Check if the player has won or loosed
            Parameters
            ----------
            good_positions : int
                The color at the good positions presents in the combination
            Return
            -------
            True if the player has won, False otherwise
        """
        if good_positions == self.__combination_nb:
            return True
        return False

    def easy_game_rules(self):
        """
            Change the rule for a easy game
        """
        self.__game_mode = "easy"
        self.__max_attempt = 10
        self.__max_color = 6
        self.__combination_nb = 4

    def normal_game_rules(self):
        """
            Change the rule for a normal game
        """
        self.__game_mode = "normal"
        self.__max_attempt = 10
        self.__max_color = 6
        self.__combination_nb = 4

    def super_game_rules(self):
        """
            Change the rule for a super game
        """
        self.__game_mode = "super"
        self.__max_attempt = 12
        self.__max_color = 8
        self.__combination_nb = 5

    @property
    def game_mode(self):
        """
            Accessor for the game mode
            Return
            -------
            The game mode
        """
        return self.__game_mode

    @property
    def score(self):
        """
            Accessor for the current score
            Return
            -------
            The current score
        """
        return self.__score

    @property
    def game_path(self):
        """
            Accessor for the game path
            Return
            -------
            The game path
        """
        return self.__game_path[:]

if __name__ == "__main__":
    my_game = Game()
    my_game.pseudo = "alex210501"
    print(f'The current pseudo is {my_game.pseudo}')
    my_game.create_random_combination()
