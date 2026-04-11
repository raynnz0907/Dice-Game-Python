import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value , max_value )

    return roll    

while True:
    players = input("Enter the number of players(2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2 - 4 players")

    else:
        print("invalid input, try agian.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_index in range(players):
        print("\n Player number", player_index + 1, "turn has just started")
        current_score = 0
