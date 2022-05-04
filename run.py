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

while True:
    user_input = input("Type rock, paper, scissor")