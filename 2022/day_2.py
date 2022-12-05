"""Solution to Day 2"""

# A = Rock
# B = Paper
# C = Scissors

# X = Rock / Lose
# Y = Paper / Draw
# Z = Scissors / win

# Scoring
# 1 for Rock, 2 for Paper, 3 for Scissors
# 0 for L, 3 for D, 6 for W


def get_strategy_score(opponent, suggestion):
    """return set for outcome score in shape of [outcome score, shape score]"""
    if opponent == 'A':
        if suggestion == 'X':
            return [0, 3]
        elif suggestion == 'Y':
            return [3, 1]
        elif suggestion == 'Z':
            return [6, 2]
    elif opponent == 'B':
        if suggestion == 'X':
            return [0, 1]
        elif suggestion == 'Y':
            return [3, 2]
        elif suggestion == 'Z':
            return [6, 3]
    elif opponent == 'C':
        if suggestion == 'X':
            return [0, 2]
        elif suggestion == 'Y':
            return [3, 3]
        elif suggestion == 'Z':
            return [6, 1]


def main():
    """Program main method"""
    total_score = 0
    with open('day_2_input.txt', encoding="utf8") as f:
        for line in f:
            [opponent, suggestion] = line.strip().split(' ')
            outcome = get_strategy_score(opponent, suggestion)
            total_score += sum(outcome)

    print(total_score)


main()
