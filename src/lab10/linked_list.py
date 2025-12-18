# класс Node — узел односвязного списка
class Node:
    def __init__(self, value, next=None):
        # значение, которое хранится в узле
        self.value = value
        # ссылка на следующий узел или None, если узел последний
        self.next = next


# класс односвязного списка
class SinglyLinkedList:
    def __init__(self):
        # ссылка на первый элемент списка
        self.head = None
        # ссылка на последний элемент списка
        self.tail = None
        # количество элементов в списке
        self._size = 0

    def append(self, value):
        # создаём новый узел 
        node = Node(value)
        # если список пуст
        if not self.head:
            # новый узел становится и головой, и хвостом
            self.head = self.tail = node
        else:
            # текущий хвост указывает на новый узел
            self.tail.next = node
            # обновляем хвост списка
            self.tail = node
        # увеличиваем размер списка
        self._size += 1

    def prepend(self, value):
        # создаём новый узел, который указывает на текущую голову
        node = Node(value, self.head)
        # новый узел становится головой списка
        self.head = node
        # если список был пуст
        if self._size == 0:
            # новый узел также становится хвостом
            self.tail = node
        # увеличиваем размер списка
        self._size += 1

    def insert(self, idx, value):
        # проверяем корректность индекса
        if idx < 0 or idx > self._size:
            # если индекс вне допустимого диапазона — ошибка
            raise IndexError("Index out of range")

        # если вставка в начало списка
        if idx == 0:
            self.prepend(value)
            return
        # если вставка в конец списка
        if idx == self._size:
            self.append(value)
            return

        # начинаем обход списка с головы
        current = self.head
        # доходим до узла перед нужной позицией
        for _ in range(idx - 1):
            current = current.next

        # вставляем новый узел между current и current.next
        current.next = Node(value, current.next)
        # увеличиваем размер списка
        self._size += 1

    def remove(self, value):
        # ссылка на предыдущий узел
        prev = None
        # начинаем с головы списка
        current = self.head

        # идём по списку
        while current:
            # если найден нужный элемент
            if current.value == value:
                # если удаляем не первый элемент
                if prev:
                    prev.next = current.next
                else:
                    # если удаляем голову списка
                    self.head = current.next
                # если удаляем хвост
                if current == self.tail:
                    self.tail = prev
                # уменьшаем размер списка
                self._size -= 1
                # выходим после удаления первого найденного элемента
                return
            # сдвигаем указатели
            prev = current
            current = current.next

    def __iter__(self):
        # начинаем итерацию с головы списка
        current = self.head
        # пока не дошли до конца списка
        while current:
            # возвращаем значение текущего узла
            yield current.value
            # переходим к следующему узлу
            current = current.next

    def __len__(self):
        # возвращаем количество элементов в списке
        return self._size

    def __repr__(self):
        # строковое представление списка
        return f"SinglyLinkedList({list(self)})"