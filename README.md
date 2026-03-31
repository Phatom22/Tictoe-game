
Tic Tac Toe (Python Console Game)
Overview
This is a simple two player Tic Tac Toe game built in Python.
Players take turns placing their marks (X or O) on a 3×3 grid until one player wins or the game ends in a draw.
Features
•	Interactive console gameplay
•	Board displayed after every move
•	Input validation 
•	win/draw detection
•	Alternating turns between players

Project Structure
•	sign_array: A list representing the 9 board positions
•	print_board(): Displays the current state of the board
•	check_winner(player): Checks if the given player has won
•	a_draw(): Checks if the board is full (draw condition)
•	play_game(): Main game loop that runs until win/draw

 How to Run
1.	Make sure you have Python 3.x installed.
2.	Save the code in a file, e.g. tic_tac_toe.py.
3.	Run the game in your terminal:
4.	python tic_tac_toe.py
5.	Follow the prompts to enter moves (positions 1–9).
Notes
•	Empty cells are represented by a space ' '.
Ensure sign_array is initialized as:
•	sign_array = [' ']*9
•	Positions are numbered 1–9 (left to right, top to bottom).
