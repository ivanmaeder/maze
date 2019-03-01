class Maze:
    def __init__(self):
        self.__grid = []

        self.width = 0
        self.height = 0

    def add_row(self, row):
        self.__grid.append(row)

        if (self.width == 0):
            self.width = len(row)

        self.height = len(self.__grid)

    def find_path(self):
        self.__fill_dead_ends(self.__find_dead_ends())

        return self.__final_path()

    def __final_path(self):
        x, y = self.__find_start()

        path = [(x, y)]
        square = self.__next_adjacent(x, y)
        while square:
            x, y = square
            path.append((x, y))

            if (self.__is_exit(x, y)):
                break

            self.__fill(x, y, "V")

            if (self.__is_closed_off(x, y)):
                backtrack_x, backtrack_y = path.pop()
                adjacent = self.__next_adjacent(backtrack_x, backtrack_y)

                while (not adjacent):
                    backtrack_x, backtrack_y = path.pop()
                    adjacent = self.__next_adjacent(backtrack_x, backtrack_y)

                path.append((backtrack_x, backtrack_y))
                square = adjacent
            else:
                square = self.__next_adjacent(x, y)

        return path

    def __adjacent_positions(self, x, y):
        min_x = 0
        min_y = 0
        max_x = self.width - 1
        max_y = self.height - 1

        return [(x, max(y - 1, min_y)),
                (x, min(y + 1, max_y)),
                (max(x - 1, min_x), y),
                (min(x + 1, max_x), y)]

    def __next_adjacent(self, x, y):
        debug = False

        for potential in self.__adjacent_positions(x, y):
            potential_x, potential_y = potential

            if (self.__is_opening(potential_x, potential_y)):
                return potential

    def __fill(self, x, y, letter="F"):
        self.__grid[y][x] = letter

    def __fill_dead_end(self, start_x, start_y):
        debug = False
        if (start_x == 17 and start_y == 4):
            debug = True

        self.__fill(start_x, start_y)

        fillable = self.__next_adjacent(start_x, start_y)

        while fillable:
            x, y = fillable

            if (self.__is_junction(x, y)):
                fillable = None
                break

            self.__fill(x, y)
            fillable = self.__next_adjacent(x, y)

    def __fill_dead_ends(self, dead_ends):
        for dead_end in dead_ends:
            self.__fill_dead_end(dead_end[0], dead_end[1])

    def __count_adjacent_squares_by_type(self, x, y, types):
        square_count = 0
        for potential in self.__adjacent_positions(x, y):
            potential_x = potential[0]
            potential_y = potential[1]

            if (self.__grid[potential_y][potential_x] in types):
                square_count += 1

        return square_count

    def __is_exit(self, x, y):
        return self.__is_opening(x, y) and self.__is_outer_edge(x, y)

    def __is_opening(self, x, y):
        return self.__grid[y][x] == "O"

    def __is_dead_end(self, x, y):
        return self.__count_adjacent_squares_by_type(x, y, ("X")) == 3

    def __is_junction(self, x, y):
        return self.__count_adjacent_squares_by_type(x, y, ("O", "S")) >= 2

    def __is_outer_edge(self, x, y):
        if (x != None and (x == 0 or x == self.width - 1)):
            return True

        if (y != None and (y == 0 or y == self.height - 1)):
            return True

        return False

    def __is_closed_off(self, x, y):
        return self.__count_adjacent_squares_by_type(x, y, ("X", "V")) == 4

    def __find_start(self):
        for y, row in enumerate(self.__grid):
            for x, square in enumerate(row):
                if (square == "S"):
                    return (x, y)

    def __find_dead_ends(self):
        dead_ends = []

        for y, row in enumerate(self.__grid):
            if (self.__is_outer_edge(None, y)):
                continue

            for x, square in enumerate(row):
                if (self.__is_outer_edge(x, y)):
                    continue

                if (square == "O" and self.__is_dead_end(x, y)):
                    dead_ends.append((x, y))

        return dead_ends

    def __repr__(self):
        str = ""
        for row in self.__grid:
            if (str):
                str += "\n"

            str += ("".join(row))

        return str
