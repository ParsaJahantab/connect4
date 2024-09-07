import numpy as np
class Board:
    def __init__(self):
        self.board = np.zeros((6, 7)).astype(int)
        self.empty_cells = [0, 0, 0, 0, 0, 0, 0]
        self.board_id = ""

    def print_board(self):
        print(np.flip(self.board),0)

    def set_board_id(self):
        for i in range(6):
            for j in range(7):
                self.board_id = self.board_id + str(self.board[i,j])


