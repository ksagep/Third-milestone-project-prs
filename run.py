import random

"""
Create the intro to the game and give a possibility
for the player to choose continue the game or not.
"""
print("Welcome to my computer game!")
print("It is the classic paper - rock - scissors game in python environment.")

playing = input("Do you want to play with it?\n")

if playing != "yes":
    quit("Thank you and have a nice day!")
    
print("Okay, let's play!")

user_wins = 0
computer_wins = 0

# create a list for three possible options
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type rock or paper or scissors or q to quit\n").lower()
    if user_input == "q":
        break
    # exclude possible variants that are not in options
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # for understanding: rock: 0, paper: 1, scissors:2
    computer_choice = options[random_number]
    print("Computer choice was", computer_choice + ".")

    if user_input == "rock" and computer_choice == "scissors":
        print("You won! Congratulations!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_choice == "rock":
        print("You won! Congratulations!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won! Congratulations!")
        user_wins += 1
        continue
# increase the responsiveness of the game put the 'Tie' option into it    
    elif user_input == computer_choice:
        print("It's a Tie!")
        user_wins += 0
        computer_wins += 0
        continue

    else:
        print("You lost!")
        computer_wins += 1

print("You won: " + str(user_wins) + " times.")
print("The computer won: " + str(computer_wins) + " times.")

"""
Provide solution for ZeroDivisionError when the second integer is 0.
In mathematics, division by 0 is undefined so python won't undertand this step
and it will generate an error.
"""
def divide_two_numbers(a,b):
        a = user_wins
        b = user_wins + computer_wins
        
        try:
            return a/b
        except ZeroDivisionError():
            return 0

print("You won: " + str((user_wins / (user_wins + computer_wins))*100) + " % of the game.")
print("Goodbye!")
divide_two_numbers(a,b)