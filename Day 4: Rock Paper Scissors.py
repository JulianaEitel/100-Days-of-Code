import random

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
"""
From there you will need to figure out:
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player.
"""

images = [rock, paper, scissors]

if my_choice > 0 and my_choice < 3:
    print(images[my_choice])
else:
    print("You chose and invalid number. Try again!")

print("Computer chose:")

comp_choice = random.randint(0, 2)

print(images[comp_choice])

if my_choice == 0 and comp_choice == 2:
    print("You win!")
elif my_choice == 0 and comp_choice == 1:
    print("You lose!")

elif my_choice == 1 and comp_choice == 0:
    print("You win!")
elif my_choice == 1 and comp_choice == 2:
    print("You lose!")

elif my_choice == 2 and comp_choice == 1:
    print("You win!")
elif my_choice == 2 and comp_choice == 0:
    print("You lose!")

elif my_choice == comp_choice:
    print("It's a tie!")
