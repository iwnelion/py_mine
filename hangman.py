import random

print("HANGMAN GAME")
hangman=["-|---",
         " | |",
         " | O",
         " |/|\\",
         " | |",
         " |/ \\",
         " |",
         "----"]
print(*hangman, sep='\n')
print("Find the hidden f1 driver")
print("He's very good at hiding, so it's gonna be difficult!")

words=["verstappen", "norris", "leclerc", "piastri", "sainz", "hamilton"]
lives=6

hiddenWord=words[random.randint(0, len(words)-1)]
length=len(hiddenWord)
displayWord=["_"]*length

print(" ".join(displayWord))

def guessLetters():
    global lives
    while lives>0:
        userGuess=str(input("Guess: ").lower())
        if len(userGuess)!=1:
            print("Please guess only a single letter at a time!")
            continue
        if userGuess in hiddenWord:
            print("Correct!")
            for i in range(length):
                if hiddenWord[i]==userGuess:
                    displayWord[i]=userGuess
            print(" ".join(displayWord))
            if "_" not in displayWord:
                print("Congratulations! You won!")
                return
        else:
            print("Incorrect!")
            lives-=1
            print("You have ", lives, " lives left.")
            hangman.pop()
            print(*hangman, sep='\n')
            print(" ".join(displayWord))
    print("Game Over! The hidden drivers is: ", hiddenWord.capitalize())

guessLetters()
