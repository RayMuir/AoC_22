from __future__ import annotations

class Dir:

    parent : Dir
    name : str
    children : list[Dir]
    files : list[str]
    size : int

    def __init__(self, parent=None, name= "", children=[], files = [], size = 0):
        self.parent = parent
        self.name = name
        self.children = children
        self.files = files
        self.size = size

def sum_dir(node):
    node.size = sum(int(file[0]) for file in node.files)
    if len(node.children) != 0:
        for c in node.children:
            node.size =  node.size + sum_dir(c)   
    return node.size

global total
total = 0

def sum_up(node : Dir):
    if node.size <= 100000:
        global total
        total += node.size
    if len(node.children) != 0:
        for c in node.children:
            sum_up(c)
sizes = []
def get_all_sizes(node : Dir):
    if node.name != "/":
        sizes.append((node.size, node.name))
    if len(node.children) != 0:
        for c in node.children:
            get_all_sizes(c)
delete = []
def part2(root_size):
    disk = 70000000 - 30000000
    for x in sizes:
        if (root_size - x[0]) <= disk:
            delete.append(x[0])
    delete.sort()
    return delete[0]
    



def main():
    root = Dir(None, "/", [], [])
    current_node = root
    text = open("Day_7/input.txt", "r").read().split('\n')
    for x in text:
        x = x.split()
        match x[0]:
            case "$":
                match x[1]:
                    case "cd":
                        match x[2]:
                            case "..":
                                current_node = current_node.parent
                            case "/":
                                current_node = root
                            case o:
                                for y in current_node.children:
                                        if y.name == o:
                                            current_node = y
                                            break
                    case "ls":
                        pass
            case "dir":
                    new_dir = Dir(current_node, x[1],[],[])
                    if new_dir not in current_node.children:
                        current_node.children.append(new_dir)
            case _:
                if (x[0], x[1]) not in current_node.files:
                    current_node.files.append((x[0],x[1]))
    sum_dir(root)
    sum_up(root)
    get_all_sizes(root)
    print(total)
    print(part2(root.size))

if __name__ == "__main__":
    main()