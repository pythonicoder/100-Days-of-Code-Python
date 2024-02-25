#Rock paper scissors game

import random

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

game_images = [rock, paper, scissors]

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper , 2 for Scissors. \n"))
print(game_images[user_choose])

computer_choose = random.randint(0, 2)
print('computer chose:')
print(game_images[computer_choose])

# Actually this logic is faulty since according to the rules of rock paper and scissors 
# This code should be implemented in a way that is different than integer-based implementation.
# To sum up, the code below is implemented according to the way the lecturer Dr. Angela presented. 

if user_choose >= 3 or user_choose < 0:
    print('You typed invalid number. Please try again')
elif computer_choose == 0 and user_choose == 2:
    print("You lose!")
elif computer_choose > user_choose:
    print("You lose!")
elif user_choose > computer_choose:
    print("You win!")
elif user_choose == computer_choose:
    print("It's a draw!")