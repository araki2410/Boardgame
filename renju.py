#!/bin/python3

import myboard

class Tiktak:
    board = []
    w_ = 11
    h_ = 11
    victory_condition = 5
    success_code = 0 
    retry_code = -1
    gameset_code = 300
    continue_code = 100
    error_code = 900

    def __init__(self):
        self.board = myboard.Board2d(x=self.w_, y=self.h_, zero=0)

    def reset_board(self):
        self.board = myboard.Board2d(x=self.w_, y=self.h_, zero=0)

    def set_stone(self,x,y,stone):
        self.board.set_piece(x,y,stone)
    
    def show_board(self):
        self.board.show_board()

    def check_lines(self, x, y):
        ### A B C
        ### D * E
        ### F G H
        
        ## 隣接マス確認
        ## 縦 B + G
        vart = self.check_line_b(x,y) + self.check_line_g(x,y)
        ## 横 D + E
        hori = self.check_line_d(x,y) + self.check_line_e(x,y)
        ## ナナメ／
        slas = self.check_line_c(x,y) + self.check_line_f(x,y)
        ## ナナメ＼
        bsla = self.check_line_a(x,y) + self.check_line_h(x,y)
       
        #print(vart, hori, slas, bsla)
        count = max(vart,hori,slas,bsla)+1

        ## Return処理
        if count >= self.victory_condition:
            return self.gameset_code
        else:
            return self.continue_code




    def check_line_a(self,x,y):
        if 0 < x and 0 < y:
            if self.board.board[y][x] == self.board.board[y-1][x-1]:
                return 1 + self.check_line_a(x-1,y-1)
            else:
                return 0
        return 0

    def check_line_b(self,x,y):
        if 0 < y:
            if self.board.board[y][x] == self.board.board[y-1][x]:
                return 1 + self.check_line_b(x,y-1)
            else:
                return 0
        return 0

    def check_line_c(self,x,y):
        if x < self.w_-1 and 0 < y:
            if self.board.board[y][x] == self.board.board[y-1][x+1]:
                return 1 + self.check_line_c(x+1,y-1)
            else:
                return 0
        return 0

    def check_line_d(self,x,y):
        if 0 < x:
            if self.board.board[y][x] == self.board.board[y][x-1]:
                return 1 + self.check_line_d(x-1,y)
            else:
                return 0
        return 0

    def check_line_e(self,x,y):
        if x < self.w_-1:
            if self.board.board[y][x] == self.board.board[y][x+1]:
                return 1 + self.check_line_e(x+1,y)
            else:
                return 0
        return 0

    def check_line_f(self,x,y):
        if 0 < x and y < self.h_-1:
            if self.board.board[y][x] == self.board.board[y+1][x-1]:
                return 1 + self.check_line_f(x-1,y+1)
            else:
                return 0
        return 0
 
    def check_line_g(self,x,y):
        if y < self.h_-1:
            if self.board.board[y][x] == self.board.board[y+1][x]:
                return 1 + self.check_line_g(x,y+1)
            else:
                return 0
        return 0

    def check_line_h(self,x,y):
        if x < self.w_-1 and y < self.h_-1:
            if self.board.board[y][x] == self.board.board[y+1][x+1]:
                return 1 + self.check_line_h(x+1,y+1)
            else:
                return 0
        return 0

    def check_stone(self, x, y):
        return self.board.board[y][x]

    def play(self,x,y,stone):
        if self.check_stone(x,y) > 0:
            print("Can't play there!!", x+1,y+1)
            return self.retry_code
        else:
            self.set_stone(x,y,stone)
            self.show_board()
            if self.check_lines(x,y) == self.gameset_code:
                print("win ", stone, " !!")
                return self.gameset_code 
            return self.success_code

def get_std():
    size = 11
    print("input X and Y (1~", size, ")")
    while 1:
        inputs_ = input().split()
        try:
            x = int(inputs_[0])
            y = int(inputs_[1])
            if 0 <= x and x <= size and 0 <= y and y <= size:
                break
        except:
            print("CAUTION: input X Y (int 1 to ", size,")")
    return x, y


def __main__():
    my_board = Tiktak()
    player = ["Black", "White"]
    black_stone = 4 
    white_stone = 8
    victory_code = 200
    player_code = {
            player[0]:black_stone,
            player[1]:white_stone
            }
    status = 0
    count = 0

    while count < victory_code:
        count += 1
        x_, y_ = get_std()
        x = x_-1
        y = y_-1
        print("X: ", x, ", Y: ", y)
        turn = count % 2
        if turn == 0:
            print(count, ": ", player[turn], ": ", player_code[player[turn]])
            count += my_board.play(x,y,player_code[player[turn]]) # Give x, y, stone
        elif turn % 2 == 1:
            print(count, ": ", player[turn], ": ", player_code[player[turn]])
            count += my_board.play(x,y,player_code[player[turn]]) # Give x, y, stone


__main__()




