class Node:

    def __init__(self,board,empty_cells,maximizing):
        self.board = board
        self.empty_cells = empty_cells
        self.is_terminal = False
        self.has_won = 0
        self.score =0
        self.maximizing = maximizing
    def check_for_terminal(self):
        if self.empty_cells ==[6,6,6,6,6,6,6]:
            self.is_terminal = True
            return
        if self.check_for_win("1"):
            self.is_terminal = True
            self.has_won = 1
            return

        if self.check_for_win("2"):
            self.is_terminal = True
            self.has_won = 2
            return


    def check_for_win(self,player:str):
        win_string = player+player+player+player
        for row in self.board:
            separator = ""
            row_string = separator.join(str(i) for i in row)

            if win_string in row_string:
                return True
        transposed_matrix = [[row[i] for row in self.board] for i in range(len(self.board[0]))]
        for col in transposed_matrix:
            separator = ""
            col_string = separator.join(str(i) for i in col)

            if win_string in col_string:
                return True
        return False

    def get_score(self,player):
        opponent = "1" if player=="2" else "2"

        plus4_string = player+player+player+player
        plus3_strings = ["0"+player+player+player,player+player+player+"0",player+player,"0",player,player+"0"+player+player]
        plus2_strings = [player+player+"00",player+"0"+player+"0",player+"00"+player,"0"+player+player+"0","0"+player+"0"+player,"00"+player+player]
        minus3_string =  ["0"+opponent+opponent+opponent,opponent+opponent+opponent+"0",opponent+opponent,"0",opponent,opponent+"0"+opponent+opponent]
        for row in self.board:
            separator = ""
            row_string = separator.join(str(i) for i in row)
            if plus4_string in row_string:
                self.score += 1000000
            for score_string in plus3_strings:
                if score_string in row_string:
                    self.score += 40
            for score_string in plus2_strings:
                if score_string in row_string:
                    self.score += 5
            for score_string in minus3_string:
                if score_string in row_string:
                    self.score -= 20
            if row[3] == 2:
                self.score +=1

        transposed_matrix = [[row[i] for row in self.board] for i in range(len(self.board[0]))]
        for col in transposed_matrix:
            separator = ""

            col_string = separator.join(str(i) for i in col)

            if plus4_string in col_string:
                self.score += 100000
            for score_string in plus3_strings:
                if score_string in col_string:
                    self.score += 40
            for score_string in plus2_strings:
                if score_string in col_string:
                    self.score += 5
            for score_string in minus3_string:
                if score_string in col_string:
                    self.score -= 20

        return self.score