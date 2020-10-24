
moves_made = 0

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
current_player = 'O'

print("|".join(["1", "2", "3"]))
print("-+-+-")
print("|".join(["4", "5", "6"]))
print("-+-+-")
print("|".join(["7", "8", "9"]))

while moves_made < 9:
    moves_made += 1
    move = input(f"{current_player}'s turn to make a move. Enter a number from 1 to 9: ")
    move = int(move)
    if move == 1:
        board[0][0] = current_player
    elif move == 2:
        board[0][1] = current_player
    elif move == 3:
        board[0][2] = current_player
    elif move == 4:
        board[1][0] = current_player
    elif move == 5:
        board[1][1] = current_player
    elif move == 6:
        board[1][2] = current_player
    elif move == 7:
        board[2][0] = current_player
    elif move == 8:
        board[2][1] = current_player
    elif move == 8:
        board[2][2] = current_player

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
