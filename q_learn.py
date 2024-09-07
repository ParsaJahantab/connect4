import copy


from state import State
from board import Board
class QAgent:

    def __init__(self):

        self.state_space = {}
        self.current_state = None
        self.q_player = 1
        self.opponent = 2

    def set_players(self, q_player, opponent):
        self.q_player = q_player
        self.opponent = opponent


    def set_init_state(self):
        board = Board()
        state = State(board=board)
        board.set_board_id()
        state.reward = 1/42
        state.get_qvalue()
        self.current_state = state
        self.state_space[board.board_id] = state

    def reset_q_agent(self):
        board = Board()
        board.set_board_id()
        state = self.get_state(board_id=board.board_id)
        state.get_qvalue()
        self.current_state = state


    def action_to_be_taken(self):
        return self.current_state.get_best_action()


    def opp_move(self,action,board:Board):
        board.set_board_id()
        if self.current_state.opp_actions[action] is None:
            next_state = self.get_state(board_id=board.board_id)
            if next_state is None:
                board_copy = copy.deepcopy(board)
                next_state = self.create_state(board_copy=board_copy)
        else:
            next_state = self.current_state.opp_actions[action]
        self.current_state = next_state
        self.current_state.get_qvalue()

    def q_move(self, action, board):
        board.set_board_id()
        if self.current_state.actions[action] is None:
            next_state = self.get_state(board_id=board.board_id)
            if next_state is None:
                board_copy = copy.deepcopy(board)
                next_state = self.create_state(board_copy=board_copy)
        else:
            next_state = self.current_state.opp_actions[action]
        self.current_state = next_state
        self.current_state.get_qvalue()



    def get_state(self,board_id):
        if board_id in self.state_space:
            state = self.state_space[board_id]
            return state
        return None

    def create_state(self,board_copy):
        state = State(board=board_copy)
        self.state_space[board_copy.board_id] = state
        state.reward = 1/42
        state.get_qvalue()
        return state


