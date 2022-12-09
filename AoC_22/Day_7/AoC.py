from __future__ import annotations

class Dir:

    parent : Dir
    name : str
    children : list[Dir]
    files : list[str]

    def __init__(self, parent=None, name= "", children=[], files = []):
        self.parent = parent
        self.name = name
        self.children = children
        self.files = files
ret = []
def sum_up(node : Dir, size = 0, depth = 0):
    for n in node.children:
        sum_up(n, size, depth + 1)
    size = 0 
    for file in node.files:
        size = int(file[0]) + size
    if int(size) <= 100000: 
        ret.append(size)

def main():
    root = Dir(None, "/", [], [])
    current_node = root
    text = open("Day_7/input2.txt", "r").read().split('\n')
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
    sum_up(root)
    print(sum(ret))


        

        
    
if __name__ == "__main__":
    main()