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

possibilities = [rock, paper, scissors]

user_choice = int(input("Choose (0)rock (1)paper (2)scissors\n"))
print(possibilities[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(possibilities[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 1:
     print("You lose!")
elif user_choice == 0 and computer_choice == 2:
     print("You win!")
elif user_choice == 1 and computer_choice == 0:
     print("You win!")
elif user_choice == 1 and computer_choice == 2:
     print("You lose!")
elif user_choice == 2 and computer_choice == 0:
     print("You lose!")
elif user_choice == 2 and computer_choice == 1:
     print("You win!")
elif user_choice == computer_choice:
     print("it's draw!")
