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

game = [rock,paper,scissors]
computer_score = 0
player_score = 0

while player_score != 5 and computer_score != 5:
    player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    computer_input = random.randint(0, 2)

    if player_input < 0 or player_input >2:
        print("Zadal si zly input skus znova")
    elif player_input == 0 and computer_input == 2:
        print("Vyhral si!\n" + "player:" + game[player_input] + "computer:" + game[computer_input])
        player_score += 1
    elif player_input == 2 and computer_input == 0:
        print("Prehral si!\n" + "player:" + game[player_input] + "computer:" + game[computer_input])
        computer_score += 1
    elif player_input > computer_input:
        print("Vyhral si!\n" + "player:" + game[player_input] + "computer:" + game[computer_input])
        player_score += 1
    elif player_input < computer_input:
        print("Prehral si!\n" + "player:" + game[player_input] + "computer:" + game[computer_input])
        computer_score += 1
    elif player_input == computer_input:
        print("Remíza!\n" + "player:" + game[player_input] + " computer:" + game[computer_input])

if computer_score == 5:
    print("Vyhral Pc")
else:
    print("Vyhral si")


