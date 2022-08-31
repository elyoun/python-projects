import random
import os
from PyDictionary import PyDictionary
from sort_list import sort_dict
from timeit import default_timer

dictionary=PyDictionary()
file = open(r'C:\Users\joaofesoares\Desktop\fizzbuzz\words.txt')

def clear_console():
    os.system('cls')

word_list = file.read().splitlines()

class hang_word:
    def __init__(self, letters):
        

        word_list2 = sort_dict(word_list)

        if (letters == 4):
            key = random.randint(1, 4)
        
        elif (letters == 7):
            key = random.randint(5,7)
        
        elif (letters == 10):
            key = random.randint(8,10)
        
        else:
            key = random.randint(9,14)

        random_num = random.randint(0, len(word_list2[key])-1)


        word_list2 = word_list2[key]

        self.word = str(word_list2[random_num])
        self.meaning = dictionary.meaning(self.word)
        
    def getWord(self):
        return self.word

    #Helper function to initialize secret word
    def mkDash(self):
        str = ""
        for i in range(len(self.word)):
            str = str + "_"
        return str


def game():
    #Choose difficulty
    print("1- 8 lives | up to 4 letters")
    print("2- 5 lives | up to 7 letters")
    print("3 - 3 lives | up to 10 letters")
    print("4 - 2 lives | up to 14 letters\n")
    
    difficulty = int(input("Select your difficulty: "))

    if (difficulty == 1):
        lives = 8
        letters = 4
    elif (difficulty == 2):
        lives = 5
        letters = 7
    elif (difficulty == 3):
        lives = 3
        letters = 10
    else:
        lives = 2
        letters = 14


    #Initialize variables    
    wrongs = []
    word1 = hang_word(letters)
    word_guess = word1.mkDash()
    #print(word_guess)
    #print(word1.getWord())

    word_guess = list(word_guess)
    word = list(word1.getWord())
    finished = False

    print("\n")
    print("this word has "+ str(len(word)) + " letters.\n")


    #Main structure of game
    while((word != word_guess) & (finished == False)):
        
        print("You have " + str(lives) + " lives")

        if(lives == 0):
            print("Game over!! The word was: " + word1.getWord())
            finished = True
            break
            
        print("Wrong guesses: " + str(wrongs) + "\n")
        print("Type 'hint' if you want a hint\n")
        guess = input("Enter your guess(or hint): ").lower()
        print("\n")

        if (list(guess) == word):
            finished = True
            break
        
        elif (guess == "hint"):
            print(str(word1.meaning) + "\n")

        elif (guess in word):
            for i in range(len(word)):
                if (guess == word[i]):
                    word_guess[i] = guess
        else:
            wrongs.append(guess)
            lives = lives - 1
            print("Wrong guess\n")


        print("Word: " + str(word_guess) + "\n")

    if(lives > 0):
        print("Congrats! You won! The word was in fact: " + word1.getWord() + ". You took " + str(default_timer()-start) + " seconds to guess it.")



#Program Structure
option = input("Do you want to play? (y/n): ").lower()
print("\n")
while(option == 'y'):
    start = default_timer()
    clear_console()
    game()
    option = input("Do you want to play again? (y/n): ").lower()

print("Thanks for playing!")


