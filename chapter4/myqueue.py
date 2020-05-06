from node import Node


class Queue:
    def __init__(self):
        self.top = None
        self.first = None
    
    def __iter__(self):
        node = self.first
        yield node
        while node.next:
            yield node.next
            node = node.next
    
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node)
        return ' - '.join([str(node.data) for node in nodes])

    def add(self, node):
        if self.is_empty():
            self.top = node 
            self.first = node
        else:
            self.top.next = node 
            self.top = node

    def remove(self):
        if self.first.next:
            self.first = self.first.next
        else:
            self.first = None
            self.top = None
    
    def peek(self):
        return self.first
    
    def is_empty(self):
        if self.top:
            return False
        return True