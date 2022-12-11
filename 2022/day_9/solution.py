"""Solution to Day 9"""


def move_head(head_pos, direction):
    """Move the head to its new location"""
    x_pos, y_pos = head_pos
    match direction:
        case "R":
            return (x_pos + 1, y_pos)
        case "U":
            return (x_pos, y_pos + 1)
        case "L":
            return (x_pos - 1, y_pos)
        case "D":
            return (x_pos, y_pos - 1)


def move_tail(head_pos, tail_pos):
    """Move the tail to match the new head location"""
    head_x, head_y = head_pos
    tail_x, tail_y = tail_pos

    # no move
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_pos

    # moved y-dir 1 space
    elif head_x == tail_x:
        if head_y > tail_y:
            return (tail_x, tail_y + 1)
        else:
            return (tail_x, tail_y - 1)

    # moved x-dir 1 space
    elif head_y == tail_y:
        if head_x > tail_x:
            return (tail_x + 1, tail_y)
        else:
            return (tail_x - 1, tail_y)

    # moved diagonally with space
    else:
        # up and right
        if head_x > tail_x and head_y > tail_y:
            return (tail_x + 1, tail_y + 1)
        # down and left
        elif head_x < tail_x and head_y < tail_y:
            return (tail_x - 1, tail_y - 1)
        # up and left
        elif head_x < tail_x and head_y > tail_y:
            return (tail_x - 1, tail_y + 1)
        # down and right
        else:
            return (tail_x + 1, tail_y - 1)


def print_grid(points):
    "display all the points visited"
    max_x, max_y = 0, 0
    for point in points:
        x_pos, y_pos = point
        if x_pos > max_x:
            max_x = x_pos
        if y_pos > max_y:
            max_y = y_pos

    grid = []
    for _ in range(max_y + 1):
        new_row = []
        for _ in range(max_x + 1):
            new_row.append('.')
        grid.append(new_row)

    for point in points:
        x_pos, y_pos = point
        grid[y_pos][x_pos] = '#'

    for row in grid:
        print(''.join(row))


def main():
    """Program main"""

    # part 1
    with open('input.txt', encoding="utf8") as file:
        curr_head_pos = (0, 0)
        curr_tail_pos = (0, 0)
        visited_tail_pos = {curr_tail_pos}
        for line in file:
            direction, spaces = [
                int(item) if item.isdigit() else item for item in line.strip().split()
            ]
            for _ in range(spaces):
                curr_head_pos = move_head(curr_head_pos, direction)
                curr_tail_pos = move_tail(curr_head_pos, curr_tail_pos)
                visited_tail_pos.add(curr_tail_pos)

        print(len(set(visited_tail_pos)))

    # part 2
    with open('input.txt', encoding="utf8") as file:
        knots = [(0, 0) for _ in range(10)]
        visited = {knots[9]}
        for line in file:
            direction, spaces = [
                int(item) if item.isdigit() else item for item in line.strip().split()
            ]
            for _ in range(spaces):
                for idx, knot in enumerate(knots):
                    if idx == 0:
                        knots[idx] = move_head(knot, direction)
                    else:
                        knots[idx] = move_tail(knots[idx-1], knot)
                visited.add(knots[9])

        print(len(set(visited)))


main()
