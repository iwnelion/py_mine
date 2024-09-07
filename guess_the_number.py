import random
print("* * * GUESS-THE-NUMBER GAME * * *")

num=random.randint(1, 10)
guess=0
guess_limit=3

while guess!=num and guess_limit>0:
    guess=int(input("Guess the number (1-10): "))
    if guess==num:
        print("Congratulations! You guessed the number!")
    elif guess>num:
        print("The number is lower")
        guess_limit-=1
        print("You have",guess_limit, "guesses left")
    elif guess<num:
        print("The number is higher")
        guess_limit-=1
        print("You have", guess_limit, "guesses left")
    if guess_limit==0:
        print("Game over! The number was", num)
