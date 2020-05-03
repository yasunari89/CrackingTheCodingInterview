from node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def __iter__(self):
        node = self.top 
        yield node
        while node.next:
            yield node.next
            node = node.next
    
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node)
        return '(top) ' + ','.join([str(node.data) for node in nodes]) + ' (bottom)'

    def push(self, node):
        if self.top == None:
            self.top = node 
        else:
            node.next = self.top 
            self.top = node

    def pop(self):
        item = self.top
        self.top = self.top.next
        return item
    