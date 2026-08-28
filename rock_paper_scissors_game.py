import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")
print(f"Player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("it's tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "rock" and computer == "paper":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("you win !")
else:
    print('You lose')