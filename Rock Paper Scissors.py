import random

rock = '''
      _______
-----'   ____)
        (_____)
        (_____)
        (____)
-----.__(___)
'''

paper = '''
      _______
-----'   ____)____
            ______)
            _______)
           _______)
-----.__________)
'''

scissors = '''
      _______
-----'   ____)____
            ______)
         __________)
        (____)
-----.__(___)
'''

game_images = [rock, paper, scissors]
for x in range(3):
  print(game_images[x])
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if choice == 0 and computer_choice == 2:
  print("You win!")
elif choice == 2 and computer_choice == 0:
  print("You lose")
elif choice < computer_choice:
  print("You lose")
elif choice > computer_choice:
  print("You win!")
elif computer_choice == choice:
  print("It's a draw")
else:
  print("You typed an invalid number, you lose!") 
