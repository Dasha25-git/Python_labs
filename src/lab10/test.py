from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList

s = Stack()
s.push(1)
s.push(2)
print(s.pop())

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())

lst = SinglyLinkedList()
lst.append(1)
lst.append(2)
lst.prepend(0)
print(lst)