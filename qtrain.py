import numpy as np

from game import Game
from q_learn import  QAgent
def train():
    qlearn = QAgent()
    qlearn.set_init_state()
    Q_wins = 0
    total =0
    game = Game(True, 2, qlearn)
    game.change_ai(1)
    for i in range (3000):
        winner= game.play()
        if winner == 1:
            qlearn.current_state.reward = 1
            print(i," win for Q")
            Q_wins +=1
            total +=1
        elif winner ==2:

            qlearn.current_state.reward = -1
            print(i," win for AI")
            total += 1
        elif qlearn ==0:
            qlearn.current_state.reward = 0
            print(i," draw")

        game.reset()
        qlearn.reset_q_agent()

    print("all games : ",total)
    print("Q_wins :",Q_wins)
    return qlearn

train()

