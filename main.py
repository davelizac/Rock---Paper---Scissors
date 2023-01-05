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
💀
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]

run = True

while run:

    g_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

    if g_choice < 0 or g_choice >= 3:
        print("You chose an invalid number! YOU LOSE 💀")
        break
        
    rps_gamer = rps[g_choice]
    
    print(rps_gamer)
    
    rps_comp = random.choice(rps)
    
    print(f"\nComputer chose:\n {rps_comp}")
    
    
    if rps_gamer == rps_comp:
      print("It is a draw...\n")
    elif rps_gamer == rock and rps_comp == scissors:
      print("You win!\n")
    elif rps_gamer == scissors and rps_comp == paper:
      print("You win!\n")
    elif rps_gamer == paper and rps_comp == rock:
      print("You win!\n")
    else:
      print("You lose...\n")