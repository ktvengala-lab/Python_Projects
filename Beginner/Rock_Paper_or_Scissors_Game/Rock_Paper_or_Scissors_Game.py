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
names = [rock, paper, scissors]
user_input = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors"))

if user_input >=0 and user_input <= 2:
    print(user_input)
    print(names[user_input])

machine_input = random.randint(0,2)
print(f"machine chose:{machine_input}")
print(names[machine_input])

if user_input >=3 or user_input < 0:
    print("You typed an invalid number. You lose!")

elif machine_input == 0 and user_input == 0:
     print("Its a tie!")
elif machine_input == 1 and user_input ==0:
     print (" You lost the Game!")
elif machine_input == 1 and user_input == 1:
     print(f"its a tie!")
elif machine_input == 2 and user_input == 1:
     print(f"You lost the Game!")
elif machine_input ==2 and user_input == 2:
     print(f"its a tie!")
elif machine_input == 2 and user_input == 0:
     print(f"You won the Game!")
elif machine_input == 1 and user_input == 2:
     print(f" You won the Game!")
elif machine_input ==0 and user_input == 1:
     print (f"You won")
elif machine_input == 0 and user_input == 2:
     print (f"you lost")
else:
    print("you typed an invalid number")