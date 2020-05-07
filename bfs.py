from graph_node import GraphNode
from queue import Queue


class BFS:
    def __init__(self):
        # BFSと言われたらQueue!!
        self.queue = Queue()
    
    def search(self, root: GraphNode, value):
        if root == None: return False
        root.marked = True
        if root.data == value: return True
        self.queue.add(root)
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
