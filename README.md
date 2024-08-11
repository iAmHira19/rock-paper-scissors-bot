# Rock Paper Scissors Bot

C# Certification from Microsoft and freeCodeCamp
This repository contains a Python implementation of a Rock, Paper, Scissors bot. The bot uses a simple strategy to try and win at least 60% of the games against various opponents by analyzing the opponent's previous moves.

## Project Structure

- `RPS_game.py`: Contains the `player` function, which implements the strategy for playing Rock, Paper, Scissors.
- `simulate_match.py`: Script to test the `player` function against a mock opponent.
- `README.md`: This file, explaining the project.

## How It Works

The bot keeps track of the opponent's previous moves and tries to predict their next move based on the most common move they have played so far. It then selects a counter move to try and win the next round.

### Strategy

- **First Move**: The bot selects a random move (`Rock`, `Paper`, or `Scissors`).
- **Subsequent Moves**: The bot analyzes the opponent's most common move and selects the counter to that move:
  - If the opponent most commonly plays `Rock`, the bot plays `Paper`.
  - If the opponent most commonly plays `Paper`, the bot plays `Scissors`.
  - If the opponent most commonly plays `Scissors`, the bot plays `Rock`.

## How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/rock-paper-scissors-bot.git
    cd rock-paper-scissors-bot
    ```

2. **Run the simulation**:
    - You can test the bot by running the `simulate_match.py` script in a Python environment.

    ```bash
    python simulate_match.py
    ```

    - The script will simulate 1,000 games and display the number of games won by the bot and the opponent.

## Example Output

After running the simulation, you should see output like:


