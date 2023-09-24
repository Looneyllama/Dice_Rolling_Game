import random
rollDice = 1
while(rollDice == 1):
  first_Dice = random.randint(1, 6)
  second_Dice = random.randint(1, 6)
  total = first_Dice + second_Dice
  if(total == 7 or total == 11):
    print("You win!")
    rollDice = 0
  elif(total == 2 or total == 3 or total == 12):
    print("You lose!")
    rollDice = 0
  else:
    print("Roll again")
