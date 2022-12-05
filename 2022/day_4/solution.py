"""Solution to Day 4"""


def get_assignment_range(assignment):
    "get range for an assignment"
    [start, end] = assignment.split('-')
    return set(range(int(start), int(end) + 1))


def are_assignments_fully_overlapping(assignments):
    """Check if sets of assignments are overlapping by checking differences of sets"""
    [assignment1, assignment2] = assignments
    return len(assignment1.difference(assignment2)) == 0 or len(assignment2.difference(assignment1)) == 0


def are_assignments_partially_overlapping(assignments):
    """Check if sets of assignments are overlapping by checking differences of sets"""
    [assignment1, assignment2] = assignments
    return len(assignment1.intersection(assignment2)) > 0


def part1():
    """Program part1 method"""
    total_overlapping_sets = 0
    with open('input.txt', encoding="utf8") as f:
        for line in f:
            assignments = [get_assignment_range(assignment)
                           for assignment in line.strip().split(',')]
            if are_assignments_fully_overlapping(assignments):
                total_overlapping_sets += 1

    print(total_overlapping_sets)


def part2():
    """Program part2 method"""
    total_overlapping_sets = 0
    with open('input.txt', encoding="utf8") as f:
        for line in f:
            assignments = [get_assignment_range(assignment)
                           for assignment in line.strip().split(',')]
            if are_assignments_partially_overlapping(assignments):
                total_overlapping_sets += 1

    print(total_overlapping_sets)


# part1()
part2()
