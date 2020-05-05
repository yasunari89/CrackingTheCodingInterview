from enum import Enum


class State(Enum):
    UNVISITED = 0
    VISITED = 1
    VISITING = 2