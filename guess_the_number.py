# import section
import random # to random the number
# title
print("/033[34mWelcome to guess the number game/033[0m\nplease select the numberbetween 1 - 100")
# can change the number what ever you want but need to change the number that in the variable as well
random_number = random.randint(1,101)
# check if it same to random number
while True:
  try:
    player_pick = int(input("type your first number>> "))
    if player_pick == random_number:
      print("\033[32mYou Win!\033[0m")
      break
      
    elif player_pick > random_number:
      print("\033[33mToo High!\033[0m")
      continue

    elif player_pick < random_number:
      print("\033[33mToo Low!\033[0m")
      continue

    else:
      print("\033[31mplease enter the number\033[0m")
      continue

  except:
    print("\033[31mError\033[0m")
    break
