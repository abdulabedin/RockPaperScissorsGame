#Description: A single and multiplayer rock, paper, scissors game.

gameon = True
output = ""

def rockpaperscissors():
  global gameon
  global output
  rock = 1
  paper = 2
  scissors = 3

  if player_one == player_two:
    if player_one == rock:
      output = "It's a tie, both players chose rock"
    elif player_one == scissors:
      output = "It's a tie, both players chose scissors"
    else:
      output = "It's a tie, both players chose paper"
    print(output)

  elif player_one == rock and player_two == scissors:
    output = "Player 1 wins, rock crushes scissors"
    print(output)

  elif player_one == rock and player_two == paper:
    output = "Player 2 wins, paper covers rock"
    print(output)

  elif player_one == paper and player_two == rock:
     output = "Player 1 wins, paper covers rock"
     print(output)

  elif player_one == paper and player_two == scissors:
    output = "Player 2 wins, scissors cut paper"
    print(output)

  elif player_one == scissors and player_two == paper:
    output = "Player 1 wins, scissors cuts paper"
    print(output)

  elif player_one == scissors and player_two == rock:
    output = "Player 2 wins, rock crushes scissors"
    print(output)

  gameon = False

  f = open('output.txt', 'w')
  f.write(output)
  f.close()

  print("\n")

  play = int(input("Enter 1 to play again: "))

  if play == 1:
    print("\n")
    gameon = True


while gameon == True:
  print("Welcome to Rock, Paper, Scissors! \n")
  players = int(input("Enter 1 for single player or 2 for multiplayer: "))
  print("\n")

  if players == 1:
    player_one = int(
        input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    print("\n")
    import random
    player_two = random.randint(1, 3)

  else:
    player_one = int(
        input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    print("\n")
    player_two = int(
        input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    print("\n")

  rockpaperscissors()