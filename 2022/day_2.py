"""Solution to Day 2"""

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

# Scoring
# 1 for Rock, 2 for Paper, 3 for Scissors
# 0 for L, 3 for D, 6 for W

shape_selection_score_lookup = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

outcome_score_lookup = {
    -1: 0,
    0: 3,
    1: 6,
}


def determine_winner(opponent, suggestion):
    """return 1 for win, -1 for loss, and 0 for tie"""
    if opponent == 'A':
        if suggestion == 'X':
            return 0
        elif suggestion == 'Y':
            return 1
        elif suggestion == 'Z':
            return -1
    elif opponent == 'B':
        if suggestion == 'X':
            return -1
        elif suggestion == 'Y':
            return 0
        elif suggestion == 'Z':
            return 1
    elif opponent == 'C':
        if suggestion == 'X':
            return 1
        elif suggestion == 'Y':
            return -1
        elif suggestion == 'Z':
            return 0


def calculate_score(shape, outcome):
    """Given shape and outcome of match, return the score"""
    shape_score = shape_selection_score_lookup[shape]
    outcome_score = outcome_score_lookup[outcome]
    return shape_score + outcome_score


def main():
    """Program main method"""
    total_score = 0
    with open('day_2_input.txt', encoding="utf8") as f:
        for line in f:
            [opponent, suggestion] = line.strip().split(' ')
            outcome = determine_winner(opponent, suggestion)
            total_score += calculate_score(suggestion, outcome)

    print(total_score)


main()
