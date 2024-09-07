# 🔴🟡 Connect4 with Minimax and Q-Learning

## 📘 Overview

This project implements the classic **Connect4** game in Python, featuring a **graphical user interface (GUI)** for a more interactive playing experience. It includes two intelligent game-playing approaches:
1. **Minimax Algorithm**: Used for strategic decision-making, ensuring optimal moves for the current player.
2. **Q-Learning Agent**: A reinforcement learning agent that learns to play Connect4 through experience, improving its strategy over time.

## ✨ Features
- 🎮 **Play Connect4** in a user-friendly GUI.
- 🧠 **Minimax Algorithm**: A recursive, depth-limited tree search for optimal moves.
- 🤖 **Q-Learning Agent**: Learns the game from scratch through exploration and exploitation, improving over multiple games.
- 📈 **Adjustable difficulty** by setting the depth of the Minimax tree or the exploration rate of the Q-learning agent.

## 🧠 Algorithms
### 1. **Minimax Algorithm**
- A decision rule used for minimizing the possible loss in a worst-case scenario. This algorithm is depth-limited and evaluates possible moves to maximize a player's chances of winning while minimizing the opponent’s.

### 2. **Q-Learning**
- A reinforcement learning algorithm that allows the agent to learn through experience. The agent updates its knowledge after every game by adjusting the Q-values based on rewards for each state-action pair, eventually learning an optimal strategy.

4. Play the game in the GUI and choose to compete against:
   - The **Minimax AI**.
   - The **Q-learning agent** that learns over time.
  



## 🎓 How Q-Learning Works in This Project
- The agent starts without any knowledge of the game.
- Through playing games, it learns by trial and error using a reward-based system.
- The Q-values are updated after each game to reflect better strategies.


## 🎮 How to Play

1. **Launch the Game**:  
   Run the game by executing the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Choose Your Opponent**:  
   - **Minimax AI**: The AI makes optimal moves based on the Minimax algorithm. To choose Minimax AI use the following code :
        ```python
                q_agent = train()
                q_agent.set_players(2,1)
                game = Game(False,4,q_agent)
                game.play()
        ```
   - **Q-Learning Agent**: The agent starts with no prior knowledge but learns and improves after each game. To choose Q-Learning use the following code :
        ```python
                    game = Game(False,2,None)
                    game.play()
        ```

3. **Make Your Move**:  
   - The Connect4 board will be displayed in the GUI.
   - Select the column (1–7) where you'd like to drop your disc.
   - Your disc (🔵) will be placed, and then the opponent’s disc (🔴) will be placed automatically.

4. **Win the Game**:  
   - The objective is to connect four of your discs (horizontally, vertically, or diagonally) before your opponent does.
   - Once the game ends, the result will be displayed, and you can start a new game.
