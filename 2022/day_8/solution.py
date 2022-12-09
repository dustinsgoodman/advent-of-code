"""Solution to Day 8"""


def build_grid(file):
    """Build a MxN matrix from input"""
    grid = []
    for line in file:
        row = []
        for char in line.strip():
            row.append(int(char))
        grid.append(row)
    return grid


def check_direction(target_height, check_list):
    """given a target height and the directional list, check if the height is taller"""
    for height in check_list:
        if height >= target_height:
            return False

    return True


def is_interior_visible(grid, row, col):
    """returns if the current cell is visible"""
    target_height = grid[row][col]

    # check left
    if check_direction(target_height, grid[row][:col]):
        return True

    # check top
    if check_direction(target_height, [grid[y][col] for y in range(0, row)]):
        return True

    # check right
    if check_direction(target_height, grid[row][col+1:]):
        return True

    # check bottom
    if check_direction(target_height, [grid[y][col] for y in range(row+1, len(grid))]):
        return True

    return False


def main():
    """Program main"""
    with open('input.txt', encoding="utf8") as file:
        tree_grid = build_grid(file)
        exterior_edges = (2 * (len(tree_grid)-2)) + (2 * len(tree_grid[0]))
        interior_visible = 0

        for row_idx, row in enumerate(tree_grid[1:-1]):
            for col_idx, _ in enumerate(row[1:-1]):
                if is_interior_visible(tree_grid, row_idx + 1, col_idx + 1):
                    interior_visible += 1

        total_visible = exterior_edges + interior_visible
        print(total_visible)


main()
