theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def winGame(board,turn):

    # Check rows
    for row in ['top', 'mid', 'low']:
        if board[row + '-L'] == board[row + '-M'] == board[row + '-R'] != ' ':
            print(turn + " won!")
            return True

    # Check columns
    for col in ['L', 'M', 'R']:
        if board['top-' + col] == board['mid-' + col] == board['low-' + col] != ' ':
            print(turn + " won!")
            return True

    # Check diagonals
    if board['top-L'] == board['mid-M'] == board['low-R'] != ' ':
        print(turn + " won!")
        return True
    if board['top-R'] == board['mid-M'] == board['low-L'] != ' ':
        print(turn + " won!")
        return True

    return False

def game(board):
    turn = "X"
    for i in range(9):
        printBoard(board)
        print("Turn For ",turn,".Move On Which Space?")
        move = input()
        board[move] = turn
        if winGame(board, turn):
            printBoard(board)
            return
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    printBoard(board)
    print("It's a tie!")     

if __name__ == "__main__":
    game(theBoard)       

