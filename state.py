import random

from board import Board
ALPHA = 0.1
GAMMA = 0.0
class State:

    def __init__(self,board):
        self.board:Board = board
        self.reward = 0
        self.Q_value = 0
        self.opp_actions = [None,None,None,None,None,None,None]
        self.actions = [None,None,None,None,None,None,None]


    def get_qvalue(self):
        max_Q_value =0
        for opp_action in self.opp_actions:
            if not opp_action is None:
                if opp_action.Q_value > max_Q_value:
                    max_Q_value = opp_action.Q_value
        for action in self.actions:
            if not action is None:
                if action.Q_value > max_Q_value:
                    max_Q_value = action.Q_value
        self.Q_value = self.Q_value + ALPHA * (self.reward + GAMMA * max_Q_value - self.Q_value)

    def set_reward(self,reward):
        self.reward = reward


    def get_best_action(self):
        max_Q_value = 0
        best_action = -1
        for i in range(6):
            action = self.actions[i]
            if not action is None:
                if action.Q_value > max_Q_value:
                    if self.board.empty_cells[i]<5:
                        max_Q_value = action.Q_value
                        best_action = i
        if best_action == -1:
            while True:
                best_action = random.randint(0,6)
                if self.board.empty_cells[best_action] < 5:
                    break
        return best_action





