from node import Node
from stack import Stack
from queue import Queue
from queue_by_stacks import QueueByStacks

q = QueueByStacks()
q.add(Node(3))
q.add(Node(4))
q.add(Node(5))
print(q)
q.remove()
print(q)
q.remove()
print(q)
