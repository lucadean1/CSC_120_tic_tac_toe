#BOARD
game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]


def print_board():
    print("    0    1    2")
    for count, row in enumerate(game):
        print(count, row)


#WIN/LOSE FUNCTION

def win():
  for row in game:
    column_1 = row[0]
    column_2 = row[1]
    column_3 = row[2]

    if column_1 == column_2 == column_3 and column_1 != "-":

      if column_1 == "X":
        print("Player One Wins!")
        return True

      if column_1 == "O":
        print("Player Two Wins!")
        return True

  for i in range (0,3):

    if game[0][i] == game[1][i] == game[2][i] and game[0][i] !="-":

      if game[0][i] == "X":
        print("Player One Wins!")
        return True

      if game[0][i] == "O":
        print("Player Two Wins!")
        return True

  if game[0][0] == game[1][1] == game[2][2] and game[0][0] != "-":

    if game[0][0] == "X":
      print("Player One Wins!")
      return True

    if game[0][0] == "O":
      print("Player Two Wins!")
      return True

  if game[2][0] == game[1][1] == game[0][2] and game[2][0] != "-":

    if game[2][0] == "X":
      print("Player One Wins!")
      return True

    if game[2][0] == "O":
      print("Player Two Wins!")
      return True



print("Welcome to Tic-Tac-Toe")
print_board()
i=1
c = 0


#PLAYER 1 STARTS HERE

while i < 10:
  error = 1
  print("turn", i)

  if i % 2 == 1:
    print("Player One, it's your turn")
  # else:
  #   print("Player three, it's your turn")
#COLUMN
    while error == 1:
      try:
        c = int(input("player 1, enter column: "))
        if c < 0 or c > 2:
          print("invalid column, please try again")
          error = 1
        else:
          error = 0
      except:
        print("Please make sure you are inputing an integer from 0-2")
        error = 1
# ROW
    error = 1
    while error == 1:
      try:
        r = int(input("player 1, enter row: "))
        if r < 0 or r > 2:
          print("invalid row, please try again")
          error = 1
        else:
          error = 0
      except:
        print("Please make sure you are inputing an integer from 0-2")
        error = 1
#END TURN
    if game[r][c] == "-":
      game[r][c] = "X"

    else:
      print("there is already a marker at ", c, ", ", r, " try again")
    print_board()

  #PLAYER TWO STARTS HERE
  if i % 2 == 0:
    print("Player Two, it's your turn")
    # COLUMN
    error = 1
    while error == 1:
      try:
        c = int(input("player 2, enter column: "))
        if c < 0 or c > 2:
          print("invalid column, please try again")
          error = 1
        else:
          error = 0
      except:
        print("Please make sure you are inputing an integer from 0-2")
        error = 1
    # ROW
    error = 1
    while error == 1:
      try:
        r = int(input("player 2, enter row: "))
        if r < 0 or r > 2:
          print("invalid row, please try again")
          error = 1
        else:
          error = 0
      except:
        print("Please make sure you are inputing an integer from 0-2")
        error = 1
  #END TURN

    if game[r][c] == "-":
      game[r][c] = "O"
    else:
      print("there is already a marker at ", c, ", ", r, " try again")
    print_board()

  #PLAY AGAIN
  if win()==True or i == 9:
    playagain = input("Would you like to play again? Input 'y' to continue or enter to end game.\n")

    if playagain == 'y':
      game = [["-","-","-"],["-","-","-"],["-","-","-"]]
      i=1


    else:
      print("Goodbye")
      break

  i += 1
