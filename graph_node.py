from node import Node
from typing import List


class GraphNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.children: List[GraphNode] = []
        self.marked = False