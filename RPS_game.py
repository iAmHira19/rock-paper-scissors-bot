import random
from collections import defaultdict

# Dictionary to keep track of the opponent's moves
opponent_history = defaultdict(int)

def player(prev_play):
    # If prev_play is empty, it means it's the first move
    if prev_play == "":
        return random.choice(['R', 'P', 'S'])
    
    # Update the opponent's move history
    opponent_history[prev_play] += 1
    
    # Determine the most common move of the opponent
    most_common_move = max(opponent_history, key=opponent_history.get, default=random.choice(['R', 'P', 'S']))
    
    # Counter strategy: Choose the move that beats the most common move of the opponent
    if most_common_move == 'R':
        return 'P'  # Paper beats Rock
    elif most_common_move == 'P':
        return 'S'  # Scissors beats Paper
    elif most_common_move == 'S':
        return 'R'  # Rock beats Scissors
