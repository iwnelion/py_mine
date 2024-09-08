import random

choices=["rock", "paper", "scissors"]
pWin=0
cWin=0
player=str(input("Pick (rock, paper, scissors, or q to quit): ")).lower()
while player:
    if player=="q":
        break
    elif player in choices:
        # computer=choices[random.randint(0, 2)]
        computer=random.choice(choices)
        print("Computer: ", computer)
        if player==computer:
            print("It's a tie")
            print("You: ", pWin, " - Computer: ", cWin)
            player=str(input("Pick (rock, paper, scissors, or q to quit): ")).lower()
        elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
            print("You win!")
            pWin+=1
            print("You: ", pWin, " - Computer: ", cWin)
            player=str(input("Pick (rock, paper, scissors, or q to quit): ")).lower()
        else:
            print("Computer wins!")
            cWin+=1
            print("You: ", pWin, " - Computer: ", cWin)
            player=str(input("Pick (rock, paper, scissors, or q to quit): "))
    else:
        print("Invalid choice.")
        player=str(input("Pick (rock, paper, scissors, or q to quit): ")).lower()

print("Final score: You: ", pWin, " - Computer: ", cWin)

if pWin>cWin:
    print("You win the game!")
elif cWin>pWin:
    print("Computer wins the game!")
else:
    print("It's a tie game!")
