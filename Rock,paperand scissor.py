def playagain():
    print("WELCOME TO ROCK PAPER SCISSORS GAME")
    print("IF YOU WISH TO QUIT THE GAME,PLEASE ENTER 'Q' ")
    gamelogic()

def gamelogic():
    choice = input("enter your choice(ROCK ,PAPER OR SCISSOR)")
    if choice==opponent_choice:
        print("its a tie")
        playagain()
    elif choice=="ROCK" and opponent_choice==options[2]:
        print("YOU WON")
        playagain()
    elif choice == "SCISSORS" and opponent_choice == options[1]:
        print("YOU WON")
        playagain()
    elif choice=="Q":
        print("you have been exited from the game")

    elif choice == "PAPER" and opponent_choice == options[0]:
        print("you won")
        playagain()
    else:
        print("YOU LOSE")
        playagain()


import  random
print("WELCOME TO ROCK PAPER SCISSORS GAME")
print("IF YOU WISH TO QUIT THE GAME,PLEASE ENTER 'Q' ")
options=["ROCK","PAPER","SCISSORS"]
opponent_choice=random.choice(options)
gamelogic()


