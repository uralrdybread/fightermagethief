from random import randint

player_wins = 0
opponent_wins = 0
# winning_score = 
# Added option for win condition other than best out of 3

while player_wins < 2 and opponent_wins < 2:
    print(f"Player Score: {player_wins} Opponent Score: {opponent_wins}")
    player = input("Player, please choose the Fighter, Mage or Thief: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        opponent = "fighter"
    elif rand_num == 1:
        opponent = "mage"
    else:
        opponent = "thief"

    print(f"Opponent plays {opponent}" )

    if player == opponent:
        print("The fight is a draw!")
    elif player == "fighter":
        if opponent == "thief":
            print("The Fighter stands triumphant over the Thief")
            player_wins += 1
        else:
            print("The Fighter is no match for the Mage's arcane prowess")
            opponent_wins += 1
    elif player == "mage":
        if opponent == "fighter":
            print("The Fighter is no match for the Mage's arcane prowess")
            player_wins += 1
        else:
            print("The Mage is overwhelmed by the Thief's skill and cunning")
            opponent_wins += 1
    elif player == "thief":
        if opponent == "fighter":
            print("The fighter stands triumphant over the thief")
            opponent_wins += 1
        else:
            print("The Mage is overwhelmed by the thief's skill and cunning")
            player_wins += 1
    else:
        print("Please choose either the Fighter, Mage or Thief!")
if player_wins > opponent_wins:
    print("You are victorious!")
else:
    print("You have been defeated...")
print(f"BATTLE RESULTS... Player Score: {player_wins} Opponent Score: {opponent_wins}")
