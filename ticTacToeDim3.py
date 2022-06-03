import random
import time

def createBoard():
    # We add ten squares so the user can enter the specific number
    # 1 - 9 instead of 0 - 8
    board = [' ' for x in range(10)]
    return board

def changeSquare(board, position, symbol):
    board[position] = symbol
    return board

def isPositionValid(board, position):
    return board[position] == ' '

def isBoardFull(board):
    full = True
    for i in range(1, 10):
        if board[i] == ' ':
            full = False
    return full

def compMove(board, symbol):
    run = True
    while run:
        selection = random.randint(1, 9)
        if isPositionValid(board, selection):
            run = False
            print()
            print(f'Computer chooses square number {selection}')
            board = changeSquare(board, selection, symbol)
            printBoard(board)
    return board

def printBoard(board):
    print('-' * 12)
    print()
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print()
    print('-' * 12)

def isWinner(bo, sym):
    return ((bo[1] == sym and bo[2] == sym and bo[3] == sym) or     # First row.
            (bo[4] == sym and bo[5] == sym and bo[6] == sym) or     # Second row.
            (bo[7] == sym and bo[8] == sym and bo[9] == sym) or     # Third row.
            (bo[1] == sym and bo[4] == sym and bo[7] == sym) or     # First column.
            (bo[2] == sym and bo[5] == sym and bo[8] == sym) or     # Second column.
            (bo[3] == sym and bo[6] == sym and bo[9] == sym) or     # Third column.
            (bo[1] == sym and bo[5] == sym and bo[9] == sym) or     # First diagonal.
            (bo[3] == sym and bo[5] == sym and bo[7] == sym))       # Second diagonal.
    
def updateBoard(board, symbol):
    run = True
    while run:
        # We ask for the position until a valid one is given.
        printBoard(board)
        position = input('Select your move (1 - 9): ')
        if position.isdigit():
            position = int(position)
            if position in range(1, 10) and isPositionValid(board, position):
                board = changeSquare(board, position, symbol)
                run = False
        if run:
            print('Invalid input. Try again.')
    return board

def chooseMode():
    run = True
    while run:
        print('(1) --> One Player')
        print('(2) --> Two Players')
        option = input('Select the mode: ')
        if option.isdigit() and option in ['1', '2']:
            option = int(option)
            run = False
        if run:
            print('Invalid input. Try again.')
    return option


if __name__ == '__main__':
    board = createBoard()
    finish = False
    victory = False
    option = chooseMode()
    player = 2
    while not finish:
        if player == 1:
            player = 2
            symbol = 'X'
        else:
            player = 1
            symbol = 'O'
        if not isBoardFull(board):
            if player == 1:
                board = updateBoard(board, symbol)
            else:
                if option == 1:
                    print('Let\'s see what move the computer does...')
                    time.sleep(1.5)
                    board = compMove(board, symbol)
                else:
                    board = updateBoard(board, symbol)
            if isWinner(board, symbol):
                finish = True
                victory = True
        else:
            finish = True
    if victory:
        print()
        print(f'Victory for player {player}')
        printBoard(board)
    else:
        print('TIE!')