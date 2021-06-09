#!/bin/python3

import tiktak
import random

class Agent:
    tktk = []
    seed = 100
    # random.seed(seed)
    random_hand_rate = 0.3 # 0~1
    bp_rate = 0.2 # 0~1

    def __init__(self):
        self.tktk = tiktak.Tiktak()

    def get_input(self):
        ## ボードをみて空の場所を指定する
        ## 今はみてない
        hand = [1,2,3]
        x = random.choice(hand)
        y = random.choice(hand)
        return x, y


    def cvc_game(self):
        player = ["Black", "White"]
        black_stone = 4
        white_stone = 8
        player_code = {
                        player[0]:black_stone,
                        player[1]:white_stone
                      }
        status = 0
        count = 0
        gameset_code = self.tktk.gameset_code

        while count < gameset_code:
            count += 1
            #x_, y_ = tktk.get_std() # 標準入力を受付
            x_, y_ = self.get_input() #
            x = x_-1
            y = y_-1
            print("X: ", x, ", Y: ", y)
            turn = count % 2
            if turn == 0:
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.tktk.play(x,y,player_code[player[turn]]) # Give x, y, stone
            elif turn % 2 == 1:
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.tktk.play(x,y,player_code[player[turn]]) # Give x, y, stone
            
            if self.tktk.playable() > 0:
                print("Draw")
                break

    def play_stone(self,x_,y_,stone):
        print("X: ", x_, ", Y: ", y_)
        x = x_-1
        y = y_-1
        result_code = self.tktk.play(x,y,stone) # Give x, y, stone
        return result_code

    def player_turn(self, stone):
        x_, y_ = self.tktk.get_std() # 標準入力を受付(1~3)
        return self.play_stone(x_,y_,stone)
 
    def cpu_turn(self, stone):
        x_, y_ = self.get_input() # プログラム上で入力(1~3)
        return self.play_stone(x_,y_,stone)

    def pvc_game(self):
        player = ["Black", "White"]
        black_stone = 4
        white_stone = 8
        player_code = {
                        player[0]:black_stone,
                        player[1]:white_stone
                      }
        status = 0
        count = 0
        gameset_code = self.tktk.gameset_code

        while count < gameset_code:
            count += 1
            turn = count % 2
            if turn == 0:
       #         #x_, y_ = tktk.get_std() # 標準入力を受付
       #         x_, y_ = self.get_input() #
       #         x = x_-1
       #         y = y_-1
       #         print("X: ", x, ", Y: ", y)
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.player_turn(stone = player_code[player[turn]]) # Give stone
            elif turn % 2 == 1:
                x_, y_ = self.get_input() #
                x = x_-1
                y = y_-1
                print("X: ", x, ", Y: ", y)
                print(count, ": ", player[turn], ": ", player_code[player[turn]])
                count += self.tktk.play(x,y,player_code[player[turn]]) # Give x, y, stone
            
            if self.tktk.playable() > 0:
                ## 最後の手で勝利した時もDrawが表示されるので直す
                print("Draw")
                break

    



agent = Agent()
agent.pvc_game()


