import json

def rpsGame():

    with open("scores.json", "r") as f:
        scores = json.load(f)

    player1_wins = 0
    player2_wins = 0
    ties = 0

    while True:

        first = input("Enter rock(r), paper(p) or scissors(s) for Player 1: ")
        second = input("Enter rock(r), paper(p) or scissors(s) for Player 2: ")

        if first in ('r', 'p', 's') and second in ('r', 'p', 's'):
            if first == second:
                print(f"It's a tie!")
                ties += 1
            elif first == "r":
                if second == "s":
                    print("Rock smashes scissors! Player 1 win!")
                    player1_wins += 1
                else:
                    print("Paper covers rock! Player 2 wins!")
                    player2_wins += 1
            elif first == "p":
                if second == "r":
                    print("Paper covers rock! Player 1 wins!")
                    player1_wins += 1
                else:
                    print("Scissors cuts paper! Player 2 wins!")
                    player2_wins += 1
            elif first == "s":
                if second == "p":
                    print("Scissors cuts paper! Player 1 wins!")
                    player1_wins += 1
                else:
                    print("Rock smashes scissors! Player 2 wins!")
                    player2_wins += 1

        else:
            print("Do you even know how to play?")
        
        reset = input("Do you want to play again? (y/n)")
        if reset.lower() == 'n':
            break

    scores["player1"]["wins"] += player1_wins
    scores["player2"]["wins"] += player2_wins
    scores["ties"] += ties

    with open("scores.json", "w") as f:
        json.dump(scores, f)
            



