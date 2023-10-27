import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("HANGMAN!")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries >0:
        guess = input("please guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter ", guess)
            elif guess not in word:
                print("Your letter is not in the word, try again!")
                tries-= 1
            else:
                print("Good Job! You guessed a correct letter.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices =[i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion="".join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you have already used that letter.")
            elif guess!=word:
                print("Uh Ou! your letter is not in the word!")
                tries -=1
                guessed_words.append(word)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess, try again")
        print(display_hangman(tries))
        print(word_completion)
        print("\n") 

    if guessed:
        print("CONGRATS! You guessed the word correctly, u win!!!!")
    else:
        print("Oh no, You lose, maybe next time!")
        print("The word was " + word)

def display_hangman(tries):
    stages = [ """
                -------
                |      |
                |      O
                |     \|/
                |      |
                |     / \\
               """
                  ,
               """
                --------
                |       |
                |       O
                |      \|/
                |       |
                |      /
               """
                  ,
               
               """
                --------
                |       |
                |       O
                |      \|/
                |       |
                |      
               """
                  ,
               """
                --------
                |       |
                |       O
                |      \|
                |       |
                |      
               """
                  ,
               """
                --------
                |       |
                |       O
                |       |
                |       |
                |      
               """
                  ,
               """
                --------
                |       |
                |       O
                |     
                |       
                |      
               """
                  ,
               """
                --------
                |       |
                |       
                |     
                |       
                |      
               """
    ]

    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Wanna play again?(Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

main()