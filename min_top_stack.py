import time
from stack import Stack


class MinTopStack:
    def __init__(self, stack):
        self.stack1 = stack
        self.stack2 = Stack()
        self.sort()
    
    def __repr__(self):
        return self.stack1.__repr__()
    
    def move(self):
        if self.stack1.is_empty():
            return False
        else:
            node = self.stack1.pop()
            if self.stack2.peek() == None:
                self.stack2.push(node)
            else:
                while node.data < self.stack2.peek().data:
                    self.stack1.push(self.stack2.pop())
                    if self.stack2.peek() == None:
                        break
                self.stack2.push(node)
        return True

    def sort(self):
        move_need = True
        while move_need:
            move_need = self.move()
        while self.stack2.peek() != None:
            self.stack1.push(self.stack2.pop())
        
