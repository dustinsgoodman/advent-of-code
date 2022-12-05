"""Solution to Day 3"""
import string

GROUP_SIZE = 3
PRIORITY_LOOKUP = dict(
    zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))


def generate_groups():
    """Read input file and generate groups of 3"""
    groups = []
    with open('day_3_input.txt', encoding="utf8") as f:
        curr_line = 0
        curr_group = []
        for line in f:
            curr_group.append(line.strip())
            curr_line += 1
            if curr_line % GROUP_SIZE == 0:
                groups.append(curr_group)
                curr_group = []
    return groups


def determine_common_items(group):
    """Return set of common items from an array of strings"""
    resultant = set(group[0])
    for items in group[1:]:
        resultant = resultant.intersection(set(items))
    return resultant


def get_items_priority(items):
    """Get total score of priority items passed in"""
    return sum([PRIORITY_LOOKUP[item] for item in items])


def part1():
    """Program part1 method"""
    total_score = 0
    with open('day_3_input.txt', encoding="utf8") as f:
        for line in f:
            sack_contents = line.strip()
            middle = int(len(sack_contents)/2)
            components = [sack_contents[0:middle], sack_contents[middle:]]
            common_items = determine_common_items(components)
            total_score += get_items_priority(common_items)

    print(total_score)


def part2():
    """Program part2 method"""
    groups = generate_groups()
    total_score = 0
    for group in groups:
        common_items = determine_common_items(group)
        total_score += get_items_priority(common_items)

    print(total_score)


# part1()


part2()
