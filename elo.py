import math

# Function to calculate the Probability
def probability(rating1, rating2):
    # Calculate and return the expected score
    return 1.0 / (1 + math.pow(10, (rating1 - rating2) / 400.0))

# Function to calculate Elo rating
# K is a constant.
# outcome determines the outcome: 1 for Player A win, 0 for Player B win, 0.5 for draw.
def elo_rating(Ra, Rb, K, outcome):
    # Calculate the Winning Probability of Player B
    Pb = probability(Ra, Rb)

    # Calculate the Winning Probability of Player A
    Pa = probability(Rb, Ra)

    # Update the Elo Ratings
    Ra = Ra + K * (outcome - Pa)
    Rb = Rb + K * ((1 - outcome) - Pb)

    # Print updated ratings
    print("Updated Ratings:-")
    print(f"Ra = {Ra} Rb = {Rb}")

# Current ELO ratings
Ra = 1200
Rb = 1000

# K is a constant
K = 30

# Outcome: 1 for Player A win, 0 for Player B win, 0.5 for draw
outcome = 1

# Function call
elo_rating(Ra, Rb, K, outcome)
