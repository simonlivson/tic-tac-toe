# Tic Tac Toe in the browser, a Gradio version of my command-line game (tic_tac_toe.py)
# The check_win and check_tie functions are the same logic as in the original file

import gradio as gr
# gradio: builds a simple web page with buttons for the game


def check_win(board, player):
# returns True if player (X or O) has 3 in a row, otherwise False

    for row in board:
    # check the 3 rows, one at a time

        if row == [player, player, player]:
        # the whole row is the same symbol

            return True
            # found a win

    for col in range(3):
    # check the 3 columns

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
    # no win


def check_tie(board):
# returns True if the board is full, otherwise False

    for row in board:
    # look at each row

        if " " in row:
        # a space means there is still an empty cell

            return False
            # not a tie yet

    return True
    # no empty cell left


def new_game():
# makes a fresh state: empty board, X starts, no result yet

    return {"board": [[" "] * 3 for _ in range(3)], "player": "X", "result": ""}
    # the board is a 2D list, like in the original game


def cell_labels(state):
# turns the board into 9 button labels

    return [state["board"][r][c] for r in range(3) for c in range(3)]
    # row by row, left to right


def status_text(state):
# the line under the board: whose turn it is, or the result

    return state["result"] or f"Player {state['player']}'s turn"
    # show the result if there is one, otherwise whose turn it is


def play(index, state):
# runs one move when a cell button is clicked

    row, col = divmod(index, 3)
    # turn the button number 0-8 into a row and a column

    if state["result"] == "" and state["board"][row][col] == " ":
    # only play if the game is not over and the cell is empty

        player = state["player"]
        # the player who is moving now

        state["board"][row][col] = player
        # put X or O in the cell

        if check_win(state["board"], player):
        # did this move win?

            state["result"] = f"Player {player} wins!"
            # save the result

        elif check_tie(state["board"]):
        # no winner, but is the board full?

            state["result"] = "It's a tie!"
            # save the result

        state["player"] = "O" if player == "X" else "X"
        # switch to the next player

    return [state] + cell_labels(state) + [status_text(state)]
    # give back the new state, the 9 labels and the status line


def reset():
# starts a new game

    state = new_game()
    # fresh state

    return [state] + cell_labels(state) + [status_text(state)]
    # same outputs as play()


with gr.Blocks(title="Tic Tac Toe") as demo:
# the web page

    gr.Markdown("# Tic Tac Toe\nTwo players take turns on the same screen. X starts.")
    # title and a short explanation

    state = gr.State(new_game())
    # the game state for this browser session

    buttons = []
    # the 9 cell buttons

    for r in range(3):
    # 3 rows

        with gr.Row():
        # put 3 buttons side by side

            for c in range(3):
            # 3 columns

                buttons.append(gr.Button(" ", min_width=80))
                # one empty cell button

    status = gr.Markdown("Player X's turn")
    # whose turn it is, or the result

    restart = gr.Button("New game", variant="primary")
    # button to start again

    outputs = [state] + buttons + [status]
    # everything that changes after a click

    for i, b in enumerate(buttons):
    # connect each cell button

        b.click(lambda s, i=i: play(i, s), inputs=state, outputs=outputs)
        # clicking cell i plays a move there

    restart.click(reset, inputs=None, outputs=outputs)
    # clicking New game resets everything


if __name__ == "__main__":
# only when the file is run directly

    demo.launch()
    # start the web app
