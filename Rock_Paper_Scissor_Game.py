
# Rock Paper Scissor Game
import random

option = ("rock", "paper", "scissor")
playing = True


print("\n\t\t\t------ ROCK PAPER SCISSOR GAME ------\n")

while playing:

    player = None
    computer = random.choice(option)

    player = input("Enter Your Choice (Rock/Paper/Scissor): ").lower()

    while player not in option:
        print(f"{player} Is A Invalid Option! Try Again!\n")
        player = input("Enter Your Choice (Rock/Paper/Scissor): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
         print("It's A Tie!")

    elif player == "rock" and computer == "scissor":
            print("You Win!")

    elif player == "paper" and computer == "rock":
        print("You Win!")

    elif player == "scissor" and computer == "paper":
        print("You Win!")

    else:
        print("You Lose!")

    continue_playing = input("Do You Want To Play Again (y/n): ").lower()
    if not continue_playing == "y":
         playing = False

print("Thanks For Playing")