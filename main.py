
moves_made = 0

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'O'

print("|".join(["1", "2", "3"]))
print("-+-+-")
print("|".join(["4", "5", "6"]))
print("-+-+-")
print("|".join(["7", "8", "9"]))

while moves_made < 9:
    move = input(f"{current_player}'s turn to make a move. Enter a number from 1 to 9: ")
    move = int(move)

    row = 0
    col = 0
    if move == 1:
        row = 0
        col = 0
    elif move == 2:
        row = 0
        col = 1
    elif move == 3:
        row = 0
        col = 2
    elif move == 4:
        row = 1
        col = 0
    elif move == 5:
        row = 1
        col = 1
    elif move == 6:
        row = 1
        col = 2
    elif move == 7:
        row = 2
        col = 0
    elif move == 8:
        row = 2
        col = 1
    elif move == 8:
        row = 2
        col = 2

    board[row][col] = current_player

    if current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'

    print("|".join(board[0]))
    print("-+-+-")
    print("|".join(board[1]))
    print("-+-+-")
    print("|".join(board[2]))
    print("\n\n")

    moves_made += 1

print("|".join(board[0]))
print("-+-+-")
print("|".join(board[1]))
print("-+-+-")
print("|".join(board[2]))
print("\n\n")

