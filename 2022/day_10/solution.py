"""Solution to Day 10"""

CRT_LENGTH = 40


def populate_queue(queue):
    """populate a queue with instructions"""
    with open('input.txt', encoding="utf8") as file:
        for line in file:
            instruction = line.strip()
            if instruction == 'noop':
                queue.append(0)
            elif instruction.startswith('addx'):
                _, val = instruction.split(' ')
                queue.append(0)
                queue.append(int(val))


def main():
    """Program main"""

    # part 1
    data_register = 1
    instruction_queue = []
    populate_queue(instruction_queue)

    notable_signal_vals = []
    for idx, val in enumerate(instruction_queue):
        data_register += val
        cycle_num = idx + 1
        if cycle_num % 20 == 0 and cycle_num % 40 != 0:
            notable_signal_vals.append(cycle_num * data_register)

    print(sum(notable_signal_vals))

    # part 2
    sprite_position = 1
    crt_screen = []
    instruction_queue = []
    populate_queue(instruction_queue)

    for cycle, val in enumerate(instruction_queue):
        adjusted_cycle = cycle % CRT_LENGTH
        if adjusted_cycle in [sprite_position - 1, sprite_position, sprite_position + 1]:
            crt_screen.append('#')
        else:
            crt_screen.append('.')
        sprite_position += val

        if cycle % CRT_LENGTH == 0:
            print(''.join(crt_screen[cycle-CRT_LENGTH:cycle]))

    print(''.join(crt_screen[-CRT_LENGTH:]))


main()
