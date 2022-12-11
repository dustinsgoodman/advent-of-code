"""Solution to Day 11"""
from math import floor, lcm

INPUT_GROUPINGS = 6


class Monkey:
    """class to represent Monkey object"""

    def __init__(self, file_input):
        self.name = self.__derive_name(file_input[0])
        self.items = self.__derive_items(file_input[1])
        self.operation = self.__derive_operation(file_input[2])

        self.divisor = self.__derive_divisor(file_input[3])
        self.true_outcome = self.__derive_true_outcome(file_input[4])
        self.false_outcome = self.__derive_false_outcome(file_input[5])

        self.inspections = 0

    def inspect_item(self, worry_factor=None):
        """Run a monkey inspection"""
        worry_level = self.items.pop(0)
        worry_level = self.operation(worry_level)
        self.inspections += 1
        if worry_factor is None:
            worry_level = floor(worry_level / 3)
        else:
            worry_level = worry_level % worry_factor
        next_monkey = self.test(worry_level)
        return (next_monkey, worry_level)

    def test(self, val):
        """Run test to see target throw monkey"""
        if val % self.divisor == 0:
            return self.true_outcome
        else:
            return self.false_outcome

    def catch_item(self, item):
        """queue new item to current list"""
        self.items.append(item)

    # constructor helpers
    def __derive_name(self, name_input):
        """get the monkey name from input 'Monkey X:\n'"""
        return name_input.strip()[:-1]

    def __derive_items(self, items_input):
        """get the starting items from input 'Starting items: X, Y\n'"""
        items = items_input.strip().split(':')[-1].strip().split(', ')
        return [int(val) for val in items]

    def __derive_operation(self, operation_input):
        """create operation function from input 'Operation: new = old + X\n'"""
        find_str = 'Operation: new = '
        expr_str = operation_input.strip()[len(find_str):]
        # pylint: disable=eval-used
        return lambda val: eval(expr_str.replace('old', str(val)))
        # pylint: enable=eval-used

    def __derive_divisor(self, divisor_input):
        """determine divisor"""
        cond_str = 'Test: divisible by '
        return int(divisor_input.strip()[len(cond_str):])

    def __derive_true_outcome(self, true_input):
        """determine positive target monkey"""
        true_str = 'If true: throw to monkey '
        return int(true_input.strip()[len(true_str):])

    def __derive_false_outcome(self, false_input):
        """determine negative target monkey"""
        false_str = 'If false: throw to monkey '
        return int(false_input.strip()[len(false_str):])

    def __str__(self):
        return self.name + " " + ', '.join(map(str, self.items))


def generate_monkies(file_input):
    """generate list of Monkey objects"""
    input_groups = [file_input[idx:idx+INPUT_GROUPINGS]
                    for idx in range(0, len(file_input), INPUT_GROUPINGS)]
    monkies = [Monkey(input_group) for input_group in input_groups]

    return monkies


def calculate_monkey_business(monkies):
    """multiple largest 2 inspection counts"""
    largest = 0
    second_largest = 0
    for monkey in monkies:
        if monkey.inspections > largest:
            second_largest = largest
            largest = monkey.inspections
        elif monkey.inspections > second_largest:
            second_largest = monkey.inspections
    return largest * second_largest


def play_rounds(monkies, rounds, worry_factor=None):
    """Play the rounds game"""
    for itr in range(rounds):
        for monkey in monkies:
            for _ in range(len(monkey.items)):
                next_monkey, item = monkey.inspect_item(worry_factor)
                monkies[next_monkey].catch_item(item)

        # round checker print
        # print('Round ' + str(itr + 1))
        # for monkey in monkies:
        #     print(monkey)
        # print()

    # print("Final inspection counts:")
    # for monkey in monkies:
    #     print(monkey.name + " " + str(monkey.inspections))


def main():
    """Program main"""
    with open('input.txt', encoding="utf8") as file:
        file_input = list(
            filter(
                lambda line: line.strip() != '',
                file.readlines()
            )
        )

    # part 1
    monkies = generate_monkies(file_input)
    play_rounds(monkies, 20)
    print('Monkey Business: ', str(calculate_monkey_business(monkies)))

    # part 2
    monkies = generate_monkies(file_input)
    worry_factor = lcm(*[monkey.divisor for monkey in monkies])
    play_rounds(monkies, 10_000, worry_factor)
    print('Monkey Business: ', str(calculate_monkey_business(monkies)))


main()
