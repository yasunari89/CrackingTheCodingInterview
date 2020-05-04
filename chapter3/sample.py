from node import Node
from stack import Stack
from queue import Queue
from queue_by_stacks import QueueByStacks
from min_top_stack import MinTopStack


s = Stack()
s.push(Node(3))
s.push(Node(2))
s.push(Node(5))
s.push(Node(4))
s.push(Node(3))
print(s)

m = MinTopStack(s)
print(m)
