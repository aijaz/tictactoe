def printBoard(board):
    print("|".join(board[0]))
    print("-+-+-")
    print("|".join(board[1]))
    print("-+-+-")
    print("|".join(board[2]))
    print("\n\n")

def run():
    moves_made = 0
    game_over = False

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'O'

    print("|".join(["1", "2", "3"]))
    print("-+-+-")
    print("|".join(["4", "5", "6"]))
    print("-+-+-")
    print("|".join(["7", "8", "9"]))

    while not game_over:
        move = input(f"{current_player}'s turn to make a move. Enter a number from 1 to 9: ")
        move = int(move) - 1
        if move < 0 or move > 8 :
            print("Invalid move. Try again.")
            continue

        row = int(move / 3)
        col = move % 3

        if board[row][col] != ' ':
            print("That spot's already taken. Try again.")
            continue

        board[row][col] = current_player

        if current_player == 'O':
            current_player = 'X'
        else:
            current_player = 'O'

        printBoard(board)

        moves_made += 1

        game_over, reason = check_for_game_over(board, moves_made)

        if game_over:
            print(f"Game over: {reason}")

def check_for_game_over(board, moves_made):
    lines = (
        # 3 horizontal lines
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),

        # 3 vertical lines
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),

        # 2 diagonal lines
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
    )

    for line in lines:
        numbers = {' ': 0, 'X': 0, 'O': 0}
        for cell in line:
            row = cell[0]
            col = cell[1]
            cell_contents = board[row][col]
            numbers[cell_contents] += 1
        if numbers['X'] == 3:
            return (True, 'X won')
        elif numbers['O'] == 3:
            return (True, 'O won')

    if moves_made == 9:
        return(True, 'Board filled')

    return (False, '')

run()
