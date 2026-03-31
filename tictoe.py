#draw a board
#have palyer x and player o
#winning conditions are combination of indexe
#allow user input
#a player will be assigned with either X or 0
#if conditions for winning is not met, or a draw then the game will continue

#list with 9 empty spaces
sign_array= [' ']*9

#draw the board and fill in index positions from sign_array
def print_board():

    board = print(f"""
     {sign_array[0]}  {sign_array[1]}  {sign_array[2]}
    ---|---|---
     {sign_array[3]}  {sign_array[4]}  {sign_array[5]}
    ---|---|---
     {sign_array[6]}  {sign_array[7]}  {sign_array[8]}

    """)


#function to check if the player meets the winning condition looking at the combinations
def check_winner(player):
    # Winning conditions (rows, columns, diagonals)
    winconditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    
    for wincond in winconditions:
        if all(sign_array[i] == player for i in wincond): 
            return True
    return False

def a_draw():
    return all(space != ' ' for space in sign_array)

#function to start the game
def play_game():
    current_player = 'X'
    #to loop a countless times until checkwinner or adraw functions conditions met.
    while True:
        print_board()
        #player makes a move by chosing a number of the position they with to place
        player_move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        
        if player_move < 0 or player_move > 8 or sign_array[player_move] != ' ':
            print("Invalid move, try again.")
            continue
        
        sign_array[player_move] = current_player
        
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif a_draw():
            print_board()
            print("It's a draw!")
            break
        
        # Change player
        current_player = 'O' if current_player == "X" else 'X'
        

#calling the function to start the game
play_game()
