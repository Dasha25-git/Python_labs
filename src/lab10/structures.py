from collections import deque


class Stack:
    def __init__(self):
        self._data = [] # создаем пустой список для хранения элементов стека

    def push(self, item): 
        self._data.append(item) # добавляем новый элемент в стек

    def pop(self):
        if self.is_empty(): # если стек пуст
            raise IndexError("Ошибка")
        return self._data.pop() # удаляем и возвращаем последний элемент списка

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1] # возвращаем верхний элемент без удаления 

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data) # возвращаем кол-во элементов 


class Queue:
    def __init__(self):
        self._data = deque() # исп. для быстрого добавления и удаления элем.

    def enqueue(self, item):
        self._data.append(item) # доб. элемент в конец очереди 

    def dequeue(self):
        if self.is_empty(): # если очередь пустая
            raise IndexError("Ошибка")
        return self._data.popleft() # удаляем и возвращаем первый элемент очереди 

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0] # возвращаем первый элемент без удаления 

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)