"""Solution to Day 12"""


class GraphNode:
    """Class for graph nodes"""

    def __init__(self, label, location):
        self.label = label
        self.visited = False
        self.parent = None
        self.location = location

    def get_val(self):
        """return comparable value"""
        if self.label == 'S':
            return ord('a')
        elif self.label == 'E':
            return ord('z')
        return ord(self.label)

    def get_potential_adjacent_edges(self):
        """return all potential (x,y) pos for adjacency nodes"""
        x_pos, y_pos = self.location
        return [
            (x_pos, y_pos + 1),  # down
            (x_pos + 1, y_pos),  # right
            (x_pos, y_pos - 1),  # up
            (x_pos - 1, y_pos),  # left
        ]

    def can_move(self, target):
        """check if the move to the target node is legal"""
        return target.get_val() - self.get_val() < 2

    def mark_visited(self):
        """mark node visited for BFS"""
        self.visited = True

    def reset_node(self):
        """mark node unvisited"""
        self.visited = False
        self.parent = None

    def __str__(self):
        return self.label + " " + ','.join([str(loc) for loc in self.location])


def build_graph(file):
    """Build a MxN matrix from input"""
    grid = []
    for line in file:
        row = []
        for char in line.strip():
            node = GraphNode(char, (len(row), len(grid)))
            row.append(node)
        grid.append(row)
    return grid


def reset_graph(graph):
    """reset graph for bfs"""
    for row in graph:
        for col in row:
            col.reset_node()


def get_node_pos(graph, target):
    """Return the target pos in the graph"""
    for row_idx, row in enumerate(graph):
        for col_idx, col in enumerate(row):
            if col.label == target:
                return col_idx, row_idx

    return -1, -1  # not found


def get_all_node_pos(graph, target):
    """get all potential starts"""
    matches = []
    for row_idx, row in enumerate(graph):
        for col_idx, col in enumerate(row):
            if col.label == target:
                matches.append((col_idx, row_idx))
    return matches


def get_adjacent_edges(graph, node):
    """get all valid adjacent edges"""

    potential_edges = node.get_potential_adjacent_edges()
    adjacent_edges = []
    for edge in potential_edges:
        x_pos, y_pos = edge

        # skip candidates out of bounds
        if x_pos < 0 or x_pos >= len(graph[0]):
            continue
        if y_pos < 0 or y_pos >= len(graph):
            continue

        # check if move is valid
        candidate_node = graph[y_pos][x_pos]
        if node.can_move(candidate_node):
            adjacent_edges.append(candidate_node)

    return adjacent_edges


def bfs(graph, root):
    """perform breadth first search to target E"""
    search_queue = []
    root.mark_visited()
    search_queue.append(root)

    while len(search_queue) > 0:
        inspect_target = search_queue.pop(0)

        if inspect_target.label == 'E':
            return inspect_target

        for edge in get_adjacent_edges(graph, inspect_target):
            if edge.visited:
                continue

            edge.mark_visited()
            edge.parent = inspect_target
            search_queue.append(edge)


def shortest_path_len(node):
    """return shortest path len given a node"""
    steps = 0
    while node.parent:
        steps += 1
        node = node.parent
    return steps


def main():
    """Program main"""
    with open('input.txt', encoding="utf8") as file:
        graph = build_graph(file)
        paths = []

        # part 1
        x_pos, y_pos = get_node_pos(graph, 'S')
        target = bfs(graph, graph[y_pos][x_pos])
        steps = shortest_path_len(target)
        paths.append(steps)
        print(steps)

        start_points = get_all_node_pos(graph, 'a')
        for point in start_points:
            reset_graph(graph)

            x_pos, y_pos = point
            target = bfs(graph, graph[y_pos][x_pos])
            if target:
                steps = shortest_path_len(target)
                paths.append(steps)

        print(min(paths))


main()
