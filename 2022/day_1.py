"""Solution to Day 1"""

calories_per_elf = [0]
with open('day_1_input.txt', encoding='utf8') as f:
    for line in f:
        calories = line.strip()

        if calories == '':
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(calories)

print(max(calories_per_elf))
