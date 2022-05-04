import random

"""
Create the intro to the game and give a possibility for player to choose continue the game or not.
"""
print("Welcome to my computer game!")
print("It is the classic paper - rock - scissor game in python environment.")

playing = input("Do you want to play with it?")

if playing != "yes":
    quit("Thank you and have a nice day!")
    
print("Okay, let's play!")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock or Paper or Scissor or Q to quit").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    # for understanding: rock: 0, paper: 1, scissor:2
    computer_choice = options[random_number]
    print("Computer choice was", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissor"
        print("You won! Congratulations!")
        user_wins += 1
        continue

    if user_input == "paper" and computer_choice == "rock"
        print("You won! Congratulations!")
        user_wins += 1
        continue

    if user_input == "scissor" and computer_choice == "paper"
        print("You won! Congratulations!")
        user_wins += 1
        continue
    
print("Goodbye!")
