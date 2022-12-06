"""Solution to Day 5"""
import re


def initialize_stacks(file):
    """fetch the stacks of crates from input"""
    crates = {}
    crates_input = []
    next_line = file.readline()[:-1]
    while next_line.strip() != '':
        crates_input.append(next_line)
        next_line = file.readline()[:-1]

    crates_input.reverse()

    stack_nums = crates_input[0].strip()
    first_stack = int(stack_nums[0])
    last_stack = int(stack_nums[-1])
    for stack in range(first_stack, last_stack + 1):
        crates[stack] = []

    for row in crates_input[1:]:
        filled_row = row.ljust(last_stack * 4, ' ')
        for idx, stack in enumerate(range(first_stack + 1, last_stack * 4, 4)):
            val = filled_row[stack-1]
            if val != ' ':
                crates[idx + 1].append(val)

    return crates


def perform_moves_part_1(crate_stacks, file):
    """Parse moves and perform the operations"""
    for move in file:
        match = re.search(r"\D*(\d+)\D*(\d+)\D*(\d+)", move.strip())
        num_to_move = int(match.group(1))
        start = int(match.group(2))
        end = int(match.group(3))

        for _ in range(num_to_move):
            val = crate_stacks[start].pop()
            crate_stacks[end].append(val)


def perform_moves_part_2(crate_stacks, file):
    """Parse moves and perform the operations"""
    for move in file:
        match = re.search(r"\D*(\d+)\D*(\d+)\D*(\d+)", move.strip())
        num_to_move = int(match.group(1))
        start = int(match.group(2))
        end = int(match.group(3))

        # for _ in range(num_to_move):
        val = crate_stacks[start][-num_to_move:]
        crate_stacks[start] = crate_stacks[start][:-num_to_move]
        crate_stacks[end] += val


def part1(filename):
    """Program part1 test"""
    with open(filename, encoding="utf8") as file:
        crate_stacks = initialize_stacks(file)

        perform_moves_part_1(crate_stacks, file)

        output = ''
        for _, stack in crate_stacks.items():
            output += stack[-1]

        print(output)


def part2(filename):
    """Program part2 test"""
    with open(filename, encoding="utf8") as file:
        crate_stacks = initialize_stacks(file)

        perform_moves_part_2(crate_stacks, file)

        output = ''
        for _, stack in crate_stacks.items():
            output += stack[-1]

        print(output)


part1('test.txt')
part1('input.txt')

part2('test.txt')
part2('input.txt')
