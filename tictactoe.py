import json


BOARD = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def render():
    board_state = f" {BOARD[1]} | {BOARD[2]} | {BOARD[3]} \n" + \
                  " - + - + -\n" + \
                  f" {BOARD[4]} | {BOARD[5]} | {BOARD[6]} \n" + \
                  " - + - + -\n" + \
                  f" {BOARD[7]} | {BOARD[8]} | {BOARD[9]} \n"
    return board_state

def get_action(player):
    while True:
        try:
            action = int(input(f"{player}'s turn! Remember, Player 1 is X and Player 2 is O. Enter a number between 1-9: "))
            if action < 1 or action > 9:
                print("Please enter a number between 1-9.")
                continue
            if BOARD[action] != ' ':
                print("That space is already occupied.")
                continue
            return action
        except ValueError:
            print("Invalid input.")

def victory_message(player):
    print(render())
    return f"{player} wins!"

def check_win(player):
   winning_positions = [
       [1,2,3], [4,5,6], [7,8,9], #rows
       [1,4,7], [2,5,8], [3,6,9], #columns
       [1,5,9], [3,5,7] #diagonals
   ]
   for pos in winning_positions:
       if(BOARD[pos[0]] == BOARD[pos[1]] == BOARD[pos[2]] == player):
           return True
           

def play_t3():
    player = 'X'
    game_round = 0
    game_over = False

    with open("scores.json", "r") as f:
        scores = json.load(f)

    player1_wins = 0
    player2_wins = 0
    ties = 0

    while not game_over:

        print(render())

        action = get_action(player)
        BOARD[action] = player

        game_round += 1

        if game_round >= 4:
            if check_win(player):
                game_over = True
                print(victory_message(player))
                if player == 'X':
                    player1_wins += 1
                else:
                    player2_wins += 1
                break

        if game_round == 9:
            print(render())
            print("It's a tie!")
            ties += 1
            game_over = True
            break

        player = 'O' if player == 'X' else 'X'

    restart = input("Would you like to play again? (y/n) ")
    if restart.lower() == 'y':
        for key in BOARD:
            BOARD[key] = ' '

    

        play_t3()

    scores["player1"]["wins"] += player1_wins
    scores["player2"]["wins"] += player2_wins
    scores["ties"] += ties

    with open("scores.json", "w") as f:
        json.dump(scores, f)

    

    

if __name__ == '__main__':
    play_t3()

