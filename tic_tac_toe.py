# Mini-Project: Tic Tac Toe
# Goal: a command-line game where two players (X and O) take turns on a 3x3 grid.
# Three in a row (row, column or diagonal) wins. Full board with no winner = tie.
#
# Step 1: Represent the board as a 2D list (list of lists), each cell ' '.
# Step 2: display_board() prints the board in a readable way.
# Step 3: player_input(player) asks for row and column, checks range and that the cell is empty.
# Step 4: check_win(board, player) checks rows, columns, diagonals. Returns True or False.
# Step 5: A function that checks for a tie (board full, no winner).
# Step 6: play() runs the game with a while loop:
#         show board, get input, update board, check win, check tie, switch player.
#         After the loop, show the result.
# Tips: small helper functions, one job per function.
#
# What you learn here:
# - 2D lists
# - while and for loops
# - if / elif / else
# - functions
# - input() and string formatting

# ===== Step 1: Representing the Game Board =====

board = [[" ", " ", " "],
# row 0: a list of 3 empty cells (a space means nobody played there yet)
         [" ", " ", " "],
# row 1: the middle row, also 3 empty cells
         [" ", " ", " "]]
# row 2: the bottom row; the outer list holds the 3 rows, so board is a 2D list

# ===== Step 2: Displaying the Game Board =====

def display_board():
# a function that prints the board as a grid

    for row in board:
    # take one row (one small list) at a time

        print(f" {row[0]} | {row[1]} | {row[2]}")
        # string formatting: put the 3 cells of the row between | lines

        print("---+---+---")
        # a line under the row so the rows are separated

# ===== Step 3: Getting Player Input =====

def player_input(player):
# a function that asks the player (X or O) for a move and returns a good row and column

    while True:
    # keep asking until the player gives a valid move

        row = input(f"Player {player}, choose a row (1-3): ")
        # ask for the row; input always gives back a string, like "2"

        col = input(f"Player {player}, choose a column (1-3): ")
        # ask for the column, also as a string

        if row not in ["1", "2", "3"] or col not in ["1", "2", "3"]:
        # safety check 1: the answer must be "1", "2" or "3" (this also catches letters)

            print("Please choose 1, 2 or 3.")
            # tell the player what went wrong

            continue
            # jump back to the top of the loop and ask again

        row = int(row) - 1
        # turn "1"-"3" into the number 0-2, because list positions start at 0

        col = int(col) - 1
        # the same for the column

        if board[row][col] != " ":
        # safety check 2: the cell must still be empty (a space)

            print("This cell is taken, choose another one.")
            # tell the player the cell is used

            continue
            # ask again

        return row, col
        # both checks passed, so give back the row and column (as a tuple)

# ===== Step 4: Checking for a Winner =====

def check_win(board, player):
# returns True if player (X or O) has 3 in a row, otherwise False

    for row in board:
    # check the 3 rows, one at a time

        if row == [player, player, player]:
        # the whole row is the same symbol, for example ["X", "X", "X"]

            return True
            # found a win, so stop here

    for col in range(3):
    # check the 3 columns: col is 0, then 1, then 2

        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
        # the same column in all 3 rows has the symbol

            return True
            # found a win

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    # diagonal from top-left to bottom-right

        return True
        # found a win

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    # diagonal from top-right to bottom-left

        return True
        # found a win

    return False
    # no row, column or diagonal matched, so no win

# ===== Step 5: Checking for a Tie =====

def check_tie(board):
# returns True if the board is full (no empty cell left), otherwise False

    for row in board:
    # look at each row

        if " " in row:
        # a space means there is still an empty cell

            return False
            # the game can go on, so it is not a tie

    return True
    # no empty cell anywhere, so the board is full
    # (play() checks for a winner first, so full with no winner = tie)

# ===== Step 6: The Main Game Loop =====

def play():
# runs the whole game from start to end

    for row in board:
    # initialize the board: go over each row

        for i in range(3):
        # and over each of its 3 cells

            row[i] = " "
            # make the cell empty, so every game starts clean

    player = "X"
    # X always starts

    result = ""
    # empty means nobody won and no tie yet

    while result == "":
    # keep playing as long as there is no result

        display_board()
        # 1. show the board

        row, col = player_input(player)
        # 2. get the current player's move (unpack the tuple into row and col)

        board[row][col] = player
        # 3. update the board: put X or O in that cell

        if check_win(board, player):
        # 4. did this move win?

            result = f"Player {player} wins!"
            # save the result; the loop will stop

        if result == "" and check_tie(board):
        # 5. no winner, but is the board full?

            result = "It's a tie!"
            # save the result; the loop will stop

        if player == "X":
        # 6. switch to the next player

            player = "O"
            # after X comes O

        else:
        # otherwise the player was O

            player = "X"
            # after O comes X

    display_board()
    # the loop ended: show the final board

    print(result)
    # and the final result (winner or tie)

play()
# start the game