from kaki import hangman_print_list

HANGMAN_ASCII_ART = """ Well come to the Hangman game
 _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
THE_WORD = "hello"
set_of_the_word = set(THE_WORD)

print("The word length:" + len(THE_WORD) * "_ ")
print("Write your name!")
PLAYER_NAME = input()
print('hello, ' + PLAYER_NAME)
MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print("guess_a_letter", )
print(MAX_TRIES)
Length_of_word = len(THE_WORD) * "_ "
guess = input()
number_of_fails = 0
while MAX_TRIES > 0:
 if guess in set_of_the_word:
    print("correct")
    set_of_the_word.remove(guess)
    print("guess_a_letter")
    guess = input()
    if len(set_of_the_word) == 0:
        print("win")
        break
 else:

    print(hangman_print_list.index(number_of_fails))
    number_of_fails += 1
    MAX_TRIES -= 1
    if MAX_TRIES == 0:
        print("loss")
        break


