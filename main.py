''' This is the main file. Run this file to select and play a particular
    game.'''

from RPC import *
from tictactoe import *
from connect4 import *

game_lib = {
    1: "Rock, Paper, Scissors",
    2: "Tic-Tac-Toe",
    3: "Connect 4"
}
while True:
    print("""
Your game library:
1: Rock, Paper, Scissors,
2: "Tic-Tac-Toe",
3: "Connect 4" 
""")
    game_choice = input("""
What game would you like to play?
Input the game ID, or type 'exit' to exit.
""")

    if game_choice == '1':
        rpsGame()
        game_choice = None

    elif game_choice == '2':
        play_t3()
        game_choice = None

    elif game_choice == '3':
        play_c4()
        game_choice = None

    elif game_choice == 'exit':
        break