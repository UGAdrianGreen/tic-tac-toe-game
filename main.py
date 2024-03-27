def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn]}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == ' ':
            board[row][col] = players[turn]
            if check_win(board, players[turn]):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = (turn + 1) % 2
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    main()
