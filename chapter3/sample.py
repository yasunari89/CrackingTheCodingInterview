from node import Node
from stack import Stack

s = Stack()
s.push(Node(3))
s.push(Node(1))
s.push(Node(5))
print(s.min())
print(s)