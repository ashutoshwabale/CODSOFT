import math

# Create empty board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

# Check if a player has won
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("X"):
        return 1
    if check_winner("O"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

# AI chooses best move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"

# Main game loop
def play_game():
    print("🎮 Tic-Tac-Toe Game")
    print("You are O | AI is X")
    print("Enter positions from 0 to 8\n")
    print_board()

    while True:
        # Human move
        try:
            move = int(input("Your move (0-8): "))
            if board[move] != " ":
                print("Position already taken!")
                continue
            board[move] = "O"
        except:
            print("Invalid input!")
            continue

        print_board()

        if check_winner("O"):
            print("🎉 You win!")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

        # AI move
        ai_move()
        print("AI move:")
        print_board()

        if check_winner("X"):
            print("🤖 AI wins!")
            break
        if is_draw():
            print("🤝 It's a draw!")
            break

# Start the game
play_game()
