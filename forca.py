import random
import os
from PyDictionary import PyDictionary
from sort_list import sort_dict


dictionary=PyDictionary()
file = open(r'C:\Users\joaofesoares\Desktop\fizzbuzz\words.txt')

def clear_console():
    os.system('cls')

class hang_word:
    def __init__(self):
        word_list = file.read().splitlines()
        random_num = random.randint(0, len(word_list)-1)
        self.word = str(word_list[random_num])
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
    print("1- 8 lives")
    print("2- 5 lives")
    print("3 - 3 lives")
    print("4 - 1 life\n")
    
    difficulty = int(input("Select your difficulty: "))

    if (difficulty == 1):
        lives = 8
    elif (difficulty == 2):
        lives = 5
    elif (difficulty == 3):
        lives = 3
    else:
        lives = 1


    #Initialize variables    
    wrongs = []
    word1 = hang_word()
    word_guess = word1.mkDash()
    print(word_guess)
    print(word1.getWord())

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
            
        print("wrong guesses: " + str(wrongs) + "\n")
        print("Type 'hint' if you want a hint\n")
        guess = input("Enter your guess(or hint): ")
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
            print("wrong guess\n")


        print("Word: " + str(word_guess) + "\n")

    if(lives > 0):
        print("Congrats! You won! The word was in fact: " + word1.getWord())



#Program Structure
option = input("Do you want to play? (y/n): ")
print("\n")
while(option == 'y'):
    clear_console()
    game()
    option = input("Do you want to play again? (y/n): ")

print("Thanks for playing!")


