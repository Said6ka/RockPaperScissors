# Rock paper scissors game
# Enter input: rock, paper or scissors

import random

isGameRunning = True

while isGameRunning == True:
  userChoice = input("You can choose rock, paper or scissors. Enter Q to quit ")

  if userChoice == "Q":
    break

  choices=["rock", "paper", "scissors"]
  print("You chose, ", userChoice)
  
  # Computer randomly selects rock, paper or scissors
  
  if userChoice not in choices:
    print("You can only choose either rock, paper, or scissors!")
  else:
    computerChoice = random.choice(choices)
  
  
  print("The computer chose,", computerChoice)
  # Give a result of the two choices
  
  if computerChoice == userChoice:
    print("It's a draw!")
  
  
  if computerChoice == "rock" and userChoice == "scissors":
    print("Computers wins, rock beats scissors!")
  
  if computerChoice == "rock" and userChoice == "paper":
    print("You won, paper covers rock")
  
  if computerChoice == "scissors" and userChoice == "rock":
    print("You won, rock beats scissors!")
  
  if computerChoice == "scissors" and userChoice == "paper":
    print("Computers wins, scissors slices up paper ")
  
  if computerChoice == "paper" and userChoice == "scissors":
    print("You win, scissors slices up paper!")
  
  if computerChoice == "paper" and userChoice == "rock":
    print("You won, paper covers rock")


print("Thanks for playing!")

# Tell user who won
