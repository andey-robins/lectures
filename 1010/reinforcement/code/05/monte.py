import random


def main():
  print("Welcome to the Monty Hall Solution Simulator")
  print("The game will be run 1000 times for staying and switching.")
  switch_win_count = 0
  stay_win_count = 0

  print("Beginning simulation...")
  for i in range(1000):
    doors = setup_doors()
    choice = choose_door()
    revealed_door = reveal_door(doors, choice)

    if switch_wins(doors, revealed_door, choice):
      switch_win_count += 1

    if stay_wins(doors, revealed_door, choice):
      stay_win_count += 1

  print("Finished simulation. Results to follow.")
  print(f'The win rate of staying is {stay_win_count/1000}')
  print(f'The win rate of switching is {switch_win_count/1000}')


def choose_door():
  return random.randint(0, 2)


def setup_doors():
  car_idx = random.randint(0, 2)
  doors = ["goat", "goat", "goat"]
  doors[car_idx] = "car"
  return doors


def reveal_door(doors, choice):
  if choice == 0:
    if doors[1] == "car":
      return 2
    else:
      return 1
  elif choice == 1:
    if doors[0] == "car":
      return 2
    else:
      return 0
  else:  # choice == 2
    if doors[0] == "car":
      return 1
    else:
      return 0


def switch_wins(doors, revealed, choice):
  doors_idxs = [0, 1, 2]
  if revealed > choice:
    doors_idxs.pop(revealed)
    doors_idxs.pop(choice)
  else:
    doors_idxs.pop(choice)
    doors_idxs.pop(revealed)
  return doors[doors_idxs[0]] == "car"


def stay_wins(doors, revealed, choice):
  return doors[choice] == "car"


if __name__ == "__main__":
  main()
