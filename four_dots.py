import numpy as np

ROW_COUNT=6
COLUMN_COUNT=7
def create_board():
    board= np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
   board[row][col]=piece

def is_valid_loc(board, col):
    return board[5][col]==0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))

board=create_board()
game_over=False
turn=0

while not game_over:
    if turn == 0:
        col= int(input("player 1 make your selection(0-6):"))

        if is_valid_loc(board,col):
            row= get_next_open_row(board,col)
            drop_piece(board,row,col,1)

    else:
        col= int(input("player 2 make your selection(0-6):"))
        if is_valid_loc(board,col):
            row= get_next_open_row(board,col)
            drop_piece(board,row,col,2)

    print_board(board)

    turn+=1
    turn= turn%2
