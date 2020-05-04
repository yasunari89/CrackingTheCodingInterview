from node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def __iter__(self):
        if self.is_empty():
            yield None
        else:
            node = self.top 
            yield node
            while node.next:
                yield node.next
                node = node.next
    
    def __repr__(self):
        if self.is_empty():
            return 'None'
        nodes = []
        for node in self:
            nodes.append(node)
        return ' - '.join([str(node.data) for node in nodes])

    def push(self, node):
        if self.is_empty():
            self.top = node 
        else:
            node.next = self.top 
            self.top = node

    def pop(self):
        if self.is_empty():
            self.top = None
            item = None
        else:
            item = Node(self.top.data)
            self.top = self.top.next
        return item
    
    def is_empty(self):
        if self.top:
            return False
        return True
    
    def peek(self):
        return self.top