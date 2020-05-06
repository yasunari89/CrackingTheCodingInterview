from graph_node import GraphNode
from myqueue import Queue


class BFS:
    def __init__(self, root: GraphNode):
        self.queue = Queue()
        self.root = root
        self.root.marked = True 
        self.queue.add(root)
    
    def search(self, value):
        while not self.queue.is_empty():
            parent_node = self.queue.peek()
            self.queue.remove()
            for child_node in parent_node.children:
                if child_node.marked == False:
                    child_node.marked = True 
                    if child_node.data == value:
                        return True
                    self.queue.add(child_node)
        return False
