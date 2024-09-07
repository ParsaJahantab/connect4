import copy
import math


from node import Node
class MiniMaxTree:

    def __init__(self,board):

        self.board = board
        self.root = None

    def set_root(self):
        board_copy = copy.deepcopy(self.board.board)
        empty_cells_copy = copy.deepcopy(self.board.empty_cells)
        self.root = Node(board=board_copy,empty_cells=empty_cells_copy,maximizing=True)


    def alpha_beta_minimax(self, node, depth, alpha, beta):
        if depth ==0 or node.is_terminal:
            if node.is_terminal:
                if node.has_won== 2:
                    return None,10000000
                elif node.has_won== 1:
                    return None,-10000000
                else:
                    return None,0
            else:
                node.get_score("2")
                return None,node.score
        if node.maximizing:
            value = - 100000
            selected_col = 3
            for current_col in range (7):
                if node.empty_cells[current_col] >=6:
                    continue
                board_copy = copy.deepcopy(node.board)
                empty_cells_copy = copy.deepcopy(node.empty_cells)
                board_copy[empty_cells_copy[current_col],current_col] = 2
                empty_cells_copy[current_col] +=1
                new_node = Node(board=board_copy,empty_cells=empty_cells_copy,maximizing= not node.maximizing)
                new_node.check_for_terminal()
                new_score = self.alpha_beta_minimax(new_node, depth - 1, alpha, beta)[1]
                if new_score > value:
                    value = new_score
                    selected_col = current_col
                alpha = max(alpha,value)
                if alpha>= beta :
                    break
            return selected_col,value
        else:
            value = 1000000
            selected_col = 0
            for current_col in range (7):
                if node.empty_cells[current_col] >=6:
                    continue
                board_copy = copy.deepcopy(node.board)
                empty_cells_copy = copy.deepcopy(node.empty_cells)
                board_copy[empty_cells_copy[current_col],current_col] = 1
                empty_cells_copy[current_col] +=1
                new_node = Node(board=board_copy,empty_cells=empty_cells_copy,maximizing= not node.maximizing)
                new_node.check_for_terminal()
                new_score = self.alpha_beta_minimax(new_node, depth - 1, alpha, beta)[1]
                if new_score < value:
                    value = new_score
                    selected_col = current_col
                beta = min(beta,value)
                if alpha>= beta :
                    break
            return selected_col,value


    def minimax(self, node, depth):
        if depth ==0 or node.is_terminal:
            if node.is_terminal:
                if node.has_won== 2:
                    return None,10000000
                elif node.has_won== 1:
                    return None,-10000000
                else:
                    return None,0
            else:
                node.get_score("2")
                return None,node.score
        if node.maximizing:
            value = - 100000
            column = 3
            for col in range (7):
                if node.empty_cells[col] >=6:
                    continue
                board_copy = copy.deepcopy(node.board)
                empty_cells_copy = copy.deepcopy(node.empty_cells)
                board_copy[empty_cells_copy[col],col] = 2
                empty_cells_copy[col] +=1
                new_node = Node(board=board_copy,empty_cells=empty_cells_copy,maximizing= not node.maximizing)
                new_node.check_for_terminal()
                new_score = self.minimax(new_node, depth - 1)[1]
                if new_score >=10000 and depth == 4:
                    return col,new_score
                if new_score > value:
                    value = new_score
                    column = col
            return column,value
        else:
            value = 1000000
            column = 0
            for col in range (7):
                if node.empty_cells[col] >=6:
                    continue
                board_copy = copy.deepcopy(node.board)
                empty_cells_copy = copy.deepcopy(node.empty_cells)
                board_copy[empty_cells_copy[col],col] = 1
                empty_cells_copy[col] +=1
                new_node = Node(board=board_copy,empty_cells=empty_cells_copy,maximizing= not node.maximizing)
                new_node.check_for_terminal()
                new_score = self.minimax(new_node, depth - 1)[1]
                if new_score < value:
                    value = new_score
                    column = col
            return column,value