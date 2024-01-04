import random

class Hangman():
    '''
    This class is used to create an instance of the game Hangman.

    Args:
        word_list (list): a list of words to be included in the game.

    Attributes:
        word_list (list): a list of words from which one is selected for the player to guess.
        num_lives (int): number of lives left in the game (default = 5).
        word (str): a word randomly selected from word_list for the player to guess. 
        word_guessed (list): a list showing which letters in the word have already been guessed.
        num_lettes (int): number of unique letters remaining to be guessed in the word.
        list_of_guesses (list): a list of letters that have already been guessed.
    '''

    def __init__(self, word_list, num_lives = 5):
        '''
        Initialization of attributes listed above.
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set([letter for letter in self.word]))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        This function checks whether the guess made by the player is in the word and updates word_guessed and num_letters accordingly.
        If the guessed letter is not in the word one life will be deducted from num_lives.

        Args:
            guess (str): a single alphabetical character, the player's guess.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letters -= 1

            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            
            print(f"Word: {self.word_guessed}")

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        '''
        This function asks for input from the player to guess a letter and checks whether the input supplied is a valid 
        and whether it has been guessed previously.
        If these conditions are met, the check_guess function will be called and the letter will be appended to list_of_guesses.
        '''
        while True:
            guess = input('Please choose a letter: ')

            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    '''
    This function initiates a game of Hangman.

    Args:
        word_list (list): a list of words to be included in the game.
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
            continue
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

# List of words for the game
word_list = ['banana','apple','bluberry','watermelon','kiwi']

# Call function to initiate a game.
play_game(word_list)