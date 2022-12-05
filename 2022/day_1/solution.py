"""Solution to Day 1"""

calories_per_elf = [0]
with open('input.txt', encoding='utf8') as f:
    for line in f:
        calories = line.strip()

        if calories == '':
            calories_per_elf.append(0)
        else:
            calories_per_elf[-1] += int(calories)

sorted_calories_per_elf = sorted(calories_per_elf, reverse=True)
print(sum(sorted_calories_per_elf[0:3]))
