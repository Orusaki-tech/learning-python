import random

computer_choice = ['rock','paper','scissors']

computer_choice = random.choice(computer_choice)

users_input = input("Choose rock, paper or scissors \n")
print("I play ", computer_choice)

if users_input == computer_choice:
    print("tie")

elif users_input =='rock' and computer_choice == 'scissors':
    print("You win")
elif users_input == "paper" and computer_choice == "rock":
    print("You win")
elif users_input == "scissors" and computer_choice == "paper":
    print("You win")
else:
    print("you lose")
