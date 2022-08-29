import random
import os
from PyDictionary import PyDictionary
dictionary=PyDictionary()

def clear_console():
    os.system('cls')



#Helper function to initialize secret word
def mkDash(s: str) -> str:
    str = ""
    for i in range(len(s)):
        str = str + "_"
    return str

#Choose difficulty
print("1- 8 lives")
print("2- 5 lives")
print("3 - 3 lives")
print("4 - 1 life")

difficulty = int(input("Select your difficulty: "))

if (difficulty == 1):
    lives = 8
elif (difficulty == 2):
    lives = 5
elif (difficulty == 3):
    lives = 3
else:
    lives = 1

#Open file and select random word
file = open(r'C:\Users\joaofesoares\Desktop\fizzbuzz\words.txt')
word_list = file.read().splitlines()
random_num = random.randint(0, len(word_list)-1)
word = word_list[random_num]
store_word = word

meaning = dictionary.meaning(str(word))



#Initialize secret word(with dashes) and list of wrong guesses
wrongs = []
word_guess = mkDash(word)
print(word_guess)
word_guess = list(word_guess)
word = list(word)
print("\n")
print("this word has "+ str(len(word)) + " letters.\n")


#Main structure of game
while(word != word_guess):
    
    print("You have " + str(lives) + " lives")


    if(lives == 0):
        print("Game over!! The word was: " + store_word)
        word = word_guess
        break
        
    print("wrong guesses: " + str(wrongs) + "\n")
    print("Type 'hint' if you want a hint\n")
    guess = input("Enter your guess(or hint): ")
    print("\n")
    
    if (guess == "hint"):
        print(str(meaning) + "\n")

    elif (guess in word):
        for i in range(len(word)):
            if (guess == word[i]):
                index = i
                word_guess[i] = guess
    else:
        wrongs.append(guess)
        lives = lives - 1
        print("wrong guess\n")


    print("Word: " + str(word_guess) + "\n")

if(lives > 0):
    print("Congrats! You won")




