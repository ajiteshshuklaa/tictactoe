# Tic Tac Toe Game

# Function to initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([board[i][j] != ' ' for i in range(3) for j in range(3)])

# Function to handle player moves
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0-2): "))
            col = int(input(f"Player {player}, enter the column (0-2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid move! Row and column must be between 0 and 2.")
            elif board[row][col] != ' ':
                print("This cell is already taken. Choose another one.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")

# Main game function
def play_game():
    board = initialize_board()
    current_player = 'X'  # X always starts
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
