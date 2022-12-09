"""Solution to Day 7"""

MAX_DIR_SIZE = 100_000


class Node:
    """Class describing a tree node"""

    def __init__(self, name, is_dir, file_size=0, parent=None):
        self.name = name
        self.is_dir = is_dir
        self.file_size = file_size
        self.parent = parent
        self.children = []

    def add_child(self, node):
        """Add a child node to the current tree node"""
        assert isinstance(node, Node)
        self.children.append(node)

    def get_child(self, name):
        """Return the child by name or nothing"""
        for child in self.children:
            if child.name == name:
                return child
        return None

    def get_size(self):
        """return the size of the node"""
        if self.is_dir:
            if self.file_size > 0:
                return self.file_size
            for child in self.children:
                if child.is_dir:
                    self.file_size += child.get_size()
                else:
                    self.file_size += child.file_size

        return self.file_size

    def get_all_dir_sizes(self, results):
        """get sizes of all directories in the current tree"""
        if not self.is_dir:
            return
        else:
            results.append(self.get_size())
            for child in self.children:
                child.get_all_dir_sizes(results)

        return results

    def __str__(self, level=0):
        ret = "\t"*level + self.is_dir*"DIR " + \
            self.name + " " + str(self.file_size) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret


def parse_cmd(cmd):
    """parse commands into usable targets"""
    if cmd.startswith('$ cd'):
        return cmd.replace("$ cd ", "")  # return next directory
    elif cmd.startswith('$ ls'):
        return None  # ls is basically a noop
    elif cmd.startswith('dir'):
        return ['dir', cmd.replace("dir ", "")]
    else:
        [file_size, file_name] = cmd.split(' ')
        return [int(file_size), file_name]


def build_tree(file, root_node):
    "create the directory tree structure"
    for line in file:
        cmd = parse_cmd(line.strip())
        if isinstance(cmd, str):  # we're in a move operation
            if cmd == '/':
                current_node = root_node
            elif cmd == '..':
                current_node = current_node.parent
            else:
                current_node = current_node.get_child(cmd)
        elif isinstance(cmd, list):
            if cmd[0] == 'dir':
                current_node.add_child(
                    Node(cmd[1], True, 0, current_node)
                )
            else:
                current_node.add_child(
                    Node(cmd[1], False, cmd[0], current_node)
                )


def main():
    """Program main"""
    with open('input.txt', encoding="utf8") as file:
        root = Node('/', True, 0)
        build_tree(file, root)

    # verify tree was built correctly

    results = []
    root.get_all_dir_sizes(results)
    sum_of_dir_sizes = sum(filter(lambda val: val < MAX_DIR_SIZE, results))
    print(sum_of_dir_sizes)


main()
