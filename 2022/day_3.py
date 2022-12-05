"""Solution to Day 3"""
import string


def determine_common_items(sack_contents):
    """Find the common items in different 2 strings"""
    middle = int(len(sack_contents)/2)
    comp1 = set(sack_contents[0:middle])
    comp2 = set(sack_contents[middle:])
    return comp1.intersection(comp2)


PRIORITY_LOOKUP = dict(
    zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))


def get_items_priority(items):
    """Get total score of priority items passed in"""
    return sum([PRIORITY_LOOKUP[item] for item in items])


def main():
    """Program main method"""
    total_score = 0
    with open('day_3_input.txt', encoding="utf8") as f:
        for line in f:
            common_items = determine_common_items(line.strip())
            total_score += get_items_priority(common_items)

    print(total_score)


main()
