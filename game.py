import random
import sys
import time
import math
from board import Board
from minimaxtree import MiniMaxTree
import pygame


class Game:

    def __init__(self,train,ai,qlearn):
        self.board = Board()
        self.turn = random.randint(0,1)
        self.first_turn = self.turn
        self.BLACK = (0,0,0)
        self.WHITE = (255, 255, 255)
        self.RED = (200, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 200)
        self.depth = 4
        self.train = train
        if not train:
            pygame.init()
            self.screen = pygame.display.set_mode((350, 350))
        self.ai = ai
        self.qlearn = qlearn
        if self.qlearn is not None:
            qlearn.set_init_state()
        self.last_opp_move = None


    def reset(self):
        self.board = Board()
        self.turn = random.randint(0,1)
        self.first_turn = self.turn
        self.depth = 4
        if not self.train:
            pygame.init()
        self.last_opp_move = None

    def change_ai(self,ai):
        self.ai = ai
    def draw(self):
        self.screen.fill(self.YELLOW)
        pygame.draw.rect(self.screen, self.BLACK, (0, 0, 350, 50))
        for i in range(6):
            for j in range(7):
                pygame.draw.circle(self.screen, self.BLACK, (j * 50 + 25, i * 50 + 75), 20)

        for i in range(6):
            for j in range(7):
                if self.board.board[i, j] ==  1:
                    pygame.draw.circle(self.screen, self.BLUE, ((6 - j) * 50 + 25, (5 - i) * 50 + 75), 20)
                elif self.board.board[i, j] == 2:
                    pygame.draw.circle(self.screen, self.RED, ((6 - j) * 50 + 25, (5 - i) * 50 + 75), 20)

        pygame.display.update()
    def player_turn(self):
        while True:
            if self.turn %2 ==1:
                depth = 4
                if self.ai==0:
                    player_move = self.human_play(2)[1]

                elif self.ai==1:
                    player_move = random.randint(0,6)

                elif self.ai==2:
                    minimax_tree =  MiniMaxTree(self.board)
                    minimax_tree.set_root()
                    player_move = minimax_tree.alpha_beta_minimax(node=minimax_tree.root, depth=depth, alpha=-math.inf, beta=math.inf)[0]
                elif self.ai==3:
                    minimax_tree =  MiniMaxTree(self.board)
                    minimax_tree.set_root()
                    player_move = minimax_tree.minimax(node=minimax_tree.root, depth=depth)[0]

                if self.valid_move(player_move=player_move):
                    break



        if self.ai ==1 or (self.ai==2 and depth<=5):
            #time.sleep(2)
            pass

        if self.ai !=0 :
            self.board.board[self.board.empty_cells[player_move], player_move] = self.turn+1
            self.board.empty_cells[player_move] = self.board.empty_cells[player_move] + 1
            self.last_opp_move = player_move
            if self.qlearn is not None:
                self.qlearn.opp_move(action=player_move,board=self.board)
        return self.check_for_end(str(self.turn+1)),self.turn+1


    def qmove(self):
        player_move = self.qlearn.action_to_be_taken()
        self.board.board[self.board.empty_cells[player_move], player_move] = self.turn+1
        self.board.empty_cells[player_move] = self.board.empty_cells[player_move] + 1
        self.qlearn.q_move(player_move, self.board)
        return self.check_for_end(str(self.turn + 1)), self.turn + 1



    def valid_move(self, player_move):
        return self.board.empty_cells[player_move] < 6 and 6 >= player_move >= 0

    def check_for_end(self, player: str):
        win_string = player + player + player + player
        for row in self.board.board:
            separator = ""
            row_string = separator.join(str(i) for i in row)

            if win_string in row_string:
                return True
        transposed_matrix = [[row[i] for row in self.board.board] for i in range(len(self.board.board[0]))]
        for col in transposed_matrix:
            separator = ""
            col_string = separator.join(str(i) for i in col)

            if win_string in col_string:
                return True
        return False


    def human_play(self,player):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(self.screen, self.BLACK, (0, 0, 350, 50))

                    selected_col = event.pos[0]
                    col = 6 - int(math.floor(selected_col / 50))
                    if self.valid_move(col):
                        self.board.board[self.board.empty_cells[col], col] = self.turn + 1
                        self.board.empty_cells[col] = self.board.empty_cells[col] + 1
                        if self.check_for_end(str(player)):
                            return True,col
                        self.board.print_board()
                        self.draw()
                        return False,col


    def count_valid_moves(self):
        valid_moves =0
        for cell in self.board.empty_cells:
            if cell<5:
                valid_moves +=1
        return valid_moves

    def play(self):
        if not self.train:
            self.draw()
        while True:
            if self.count_valid_moves() == 0:
                return 0
            if self.turn==0:
                if not self.train:
                    if self.human_play(1)[0]:
                        font = pygame.font.SysFont("Arial", 36)
                        win_string = "player "+str(self.first_turn+1) +" wins"
                        txtsurf = font.render(win_string, True, self.WHITE)
                        self.board.print_board()
                        self.draw()
                        self.screen.blit(txtsurf, (65, 0))
                        pygame.display.update()
                        print("player one wins")
                        time.sleep(300)
                        return 1,self.board
                    else:
                        pass
                else:
                    if self.qmove()[0]:
                        return 1

            else:
                if self.player_turn()[0]:
                    if not self.train:
                        font = pygame.font.SysFont("Arial", 36)
                        player_to_win = 1 if self.first_turn==0 else 2
                        win_string = "player "+str((player_to_win))+ " wins"
                        txtsurf = font.render(win_string, True, self.WHITE)
                        self.board.print_board()
                        self.draw()
                        self.screen.blit(txtsurf, (65, 0))
                        pygame.display.update()
                        print("player two wins")
                        time.sleep(300)
                    return 2
            if not self.train:
                self.board.print_board()
                self.draw()
            self.turn +=1
            self.turn = self.turn %2

