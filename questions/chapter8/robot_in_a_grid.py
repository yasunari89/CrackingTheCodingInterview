from typing import List

class Cell:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

class RobotInAGrid:
    def __init__(self, off_limit: Cell=None, size=(30, 30)):
        self.memo = [[None for _ in range(size[1])] for _ in range(size[0])]
        self.off_limit = off_limit

    def count_paths(self, cell: Cell) -> int:
        if cell.x == 0 and cell.y == 0:
            return 0
        if self.off_limit:
            if cell.x == self.off_limit.x and cell.y == self.off_limit.y:
                return 0
        if cell.x < 0 or cell.y < 0:
            return 0
        elif cell.x == 1 and cell.y == 0:
            return 1
        elif cell.x == 0 and cell.y == 1:
            return 1
        else:
            if not self.memo[cell.y][cell.x]:
                self.memo[cell.y][cell.x] = self.count_paths(Cell(cell.x-1, cell.y)) + self.count_paths(Cell(cell.x, cell.y-1))
            return self.memo[cell.y][cell.x]
