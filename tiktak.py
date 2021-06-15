#!/bin/python3

import myboard
import numpy as np

class Tiktak:
    board = []
    empty_stone = [1,0,0]
    black_stone = [0,1,0]
    white_stone = [0,0,1]
    w_ = 3
    h_ = 3
    victory_condition = 3
    success_code = 0 
    retry_code = -1
    gameset_code = 300
    continue_code = 100
    error_code = 900
    empty_cel = 0

    def __init__(self):
        self.board = myboard.Board2d(x=self.w_, y=self.h_, emp=self.empty_stone)
        self.empty_stone = self.board.empty_cel

    def reset_board(self):
        self.board = myboard.Board2d(x=self.w_, y=self.h_, empty_stone=self.empty_stone)
        self.empty_stone = self.board.empty_cel

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

    def playable(self):
        # Return success_code when playable 
        # Return gameset_code when displayable 
        b_ = np.array(self.board.board).flatten()
        if np.count_nonzero(b_==0) == 0:
            #何も置かれていないマスが0箇所だった時
            return self.gameset_code
        else:
            return self.success_code

    def play(self,x,y,stone):
        # 空の場合石を置く、空でない場合リトライコードを返す、石を置いたら勝利判定を行う。
        ## 引き分け判定がない
        if self.check_stone(x,y) == self.empty_stone:
            self.set_stone(x,y,stone)
            self.show_board()
            if self.check_lines(x,y) == self.gameset_code:
                print("win ", stone, " !!")
                return self.gameset_code 
            return self.success_code
        else:
            print("Can't play there!!", x+1,y+1)
            return self.retry_code

    def get_std(self):
        # 標準入力を受付
        print("input X and Y (1~3)")
        while 1:
            inputs_ = input().split()
            try:
                x = int(inputs_[0])
                y = int(inputs_[1])
                if 0 <= x and x <= 3 and 0 <= y and y <= 3:
                    break
            except:
                print("CAUTION: input X Y (int 1 to 3)")
        return x, y


    def game(self):
        player = ["Black", "White"]
        black_stone = [0,1,0] 
        white_stone = [0,0,1]
        player_code = {
                player[0]:black_stone,
                player[1]:white_stone
                }
        status = 0
        count = 0
        game_status = 0

        while count < self.gameset_code:
            count += 1
            x_, y_ = self.get_std() # 標準入力を受付
            x = x_-1
            y = y_-1
            print("X: ", x, ", Y: ", y)
            turn = count % 2
            if turn == 0:
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.play(x,y,player_code[player[turn]]) # Give x, y, stone
            elif turn % 2 == 1:
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.play(x,y,player_code[player[turn]]) # Give x, y, stone

            game_status = self.playable()
            count += game_status
            if count > self.gameset_code:
                print("__DRAW__")
        print("__GAME SET__")

if __name__ == '__main__':
    game = Tiktak()
    game.game()





