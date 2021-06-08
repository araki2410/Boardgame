#!/bin/python3

class Board2d:
    board = []
    empty_cel = 0
    width = 9 
    height = 9
    success_code = 0
    error_code = 900

    def __init__(self, x=width,y=height, emp=empty_cel):
        # Inisialize zero padding board. as (x,y) scale.
        self.width = x
        self.height = y
        self.empty_cel = emp
        y_ = [emp] * y
        for i in range(x):
            self.board.append(y_.copy())

    def show_board(self):
        # Show board line by line.
        for i in self.board:
            print(i)
        return self.success_code

    def set_piece(self, x, y, piece):
        # Set piece on (x,y).
        if x > self.width or y > self.height:
            return self.error_code
        else:
            self.board[y][x] = piece
            return self.success_code



