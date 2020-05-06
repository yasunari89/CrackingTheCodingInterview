from stack import Stack


class QueueByStacks:
    def __init__(self):
        self.__stack1 = Stack()
        self.__stack2 = Stack()
    
    def __repr__(self):
        return self.__stack1.__repr__()

    def add(self, node):
        self.__stack1.push(node)
    
    def remove(self):
        while self.__stack1.peek():
            node = self.__stack1.pop()
            self.__stack2.push(node)
        self.__stack2.pop()
        while self.__stack2.peek():
            node = self.__stack2.pop()
            self.__stack1.push(node)
