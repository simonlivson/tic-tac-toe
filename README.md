# Tic Tac Toe (Python, command line)

A two-player tic-tac-toe game for the terminal, written in plain Python.

This was my first mini-project in the Developers Institute GenAI & ML bootcamp, at the end of the week 1 Python fundamentals.

## What it does

- Draws a 3x3 board in the terminal.
- Players X and O take turns typing a row (1-3) and a column (1-3).
- Rejects input that isn't 1, 2 or 3, and moves on a cell that is already taken.
- Checks for three in a row (rows, columns and both diagonals) after every move.
- Ends with "Player X wins!", "Player O wins!" or "It's a tie!" when the board is full.

## How to run it

You need Python 3. No extra libraries.

```
python tic_tac_toe.py
```

You can also paste the code into a Google Colab cell and run it there.

## Sample output

```
 X | X |  
---+---+---
 O | O |  
---+---+---
   |   |  
---+---+---
Player X, choose a row (1-3): 1
Player X, choose a column (1-3): 3
 X | X | X
---+---+---
 O | O |  
---+---+---
   |   |  
---+---+---
Player X wins!
```

## What I learned

- How to store a grid as a list of lists (a 2D list) and reach a cell with `board[row][col]`.
- How to keep asking for input in a `while True` loop until it is valid, using `continue` to ask again.
- That `input()` always returns a string, and that list positions start at 0, so the player's "1" becomes row 0.
- How to split a program into small functions with one job each: show the board, get a move, check for a win, check for a tie.
- Why the order of checks matters: the game checks for a winner before checking for a full board, so a winning last move isn't reported as a tie.

## Tech used

- Python 3
- Lists, loops, conditionals, functions, `input()` and f-strings

## Browser version

There is also a small Gradio version in `hf_space/` that runs the same win and tie checks with clickable buttons, for a Hugging Face Space.

## More from the bootcamp

All my bootcamp exercises: https://github.com/simonlivson/DI_Bootcamp
