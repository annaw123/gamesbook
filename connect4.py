n = 6
m = 7
board = [0] * n
for i in range(n):
    board[i] = [0] * m

def drawBoard(board):
    for row in board:
        for hole in row:
            if hole == 0:
                print('⚪', end=' ')
            elif hole == 1:
                print('🔴', end= ' ')
            elif hole == 2:
                print('🔵', end= ' ')
        print()
    print()


drawBoard(board)


def addCounter(board, column, player):
    for row_index in range(len(board)-1, 0, -1):
        if board[row_index][column] == 0:
            print(row_index)
            print('I am empty')
            board[row_index][column] = player
            break

def play2goes(c1, c2):
    addCounter(board, c1, 1)
    drawBoard(board)
    addCounter(board, c2, 2)
    drawBoard(board)

play2goes(3,4)
play2goes(2,3)
play2goes(1,0)
play2goes(3,3)
play2goes(0,1)
play2goes(2,2)