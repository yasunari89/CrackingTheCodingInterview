# https://realpython.com/linked-lists-python/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node 
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join([str(node) for node in nodes])
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node 
            node = node.next
    
    def add_first(self, node):
        node.next = self.head 
        node.head = None 
    
    def add_last(self, node):
        if not self.head:
            self.head = node 
            return 
        for current_node in self:
            pass 
        current_node.next = node
    
    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is Empty.")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return 
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return 
            previous_node = node 
        raise Exception("Node with data '{}' not found.".format(str(target_node_data)))