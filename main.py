
from game import Game
from qtrain import train
def main():
    #q_learn = train()
    game = Game(False,2,None)
    game.play()
if __name__ == '__main__':
    main()


