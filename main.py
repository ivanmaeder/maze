#!/usr/bin/env python3

import fileinput
from maze import Maze

def main():
    maze = Maze()

    for line in fileinput.input():
        maze.add_row(list(line.strip()))

    print(maze.find_path())

if __name__ == "__main__":
    main()
