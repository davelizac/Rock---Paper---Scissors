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

invalid = '''
  _____
 /     \
| () () |
 \  ^  /
  |||||
  |||||

'''

#Write your code below this line 👇

rps = [rock, paper, scissors]

g_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

invalid_choice = g_choice < 0 or g_choice >= 3 

rps_gamer = rps[g_choice]

print(rps_gamer)

rps_comp = random.choice(rps)

print(f"\nComputer chose:\n {rps_comp}")

if g_choice == invalid_choice:
  print(f"You chose an invalid number, you bimbo... YOU LOSE!\n\n {invalid}")
if rps_gamer == rps_comp:
  print("It is a draw...")
elif rps_gamer == rock and rps_comp == scissors:
  print("You win!")
elif rps_gamer == scissors and rps_comp == paper:
  print("You win!")
elif rps_gamer == paper and rps_comp == rock:
  print("You win!")
else:
  print("You lose...")