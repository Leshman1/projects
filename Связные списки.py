class Node:
    """Класс узла, который также управляет всем списком"""
    
    def __init__(self, value):
        self.value = value
        self.link_next = None
    
    # 1. Чтение всех элементов
    def display(self):
        """Вывод всех элементов списка"""
        current = self
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.link_next
        print(" -> ".join(elements))
    
    # 2. Вставка элемента в конец
    def appendToTail(self, value):
        """Добавление элемента в конец списка"""
        new_node = Node(value)
        current = self
        
        # Проходим до конца списка
        while current.link_next is not None:
            current = current.link_next
        
        current.link_next = new_node
    
    # 3. Вставка элемента в начало
    def prepend(self, value):
        """Добавление элемента в начало списка"""
        new_node = Node(value)
        new_node.link_next = self.link_next
        self.link_next = new_node
        self.value, new_node.value = new_node.value, self.value

    
    # 4. Удаление элемента с конца
    def popFromTail(self):
        """Удаление элемента с конца списка"""
        if self.link_next is None:
            # Если только один элемент
            removed_value = self.value
            # ВНИМАНИЕ: нельзя удалить сам узел изнутри
            return removed_value, None
        
        current = self
        while current.link_next and current.link_next.link_next:
            current = current.link_next
        
        removed_value = current.link_next.value
        current.link_next = None
        return removed_value, self
    
    # 5. Удаление элемента с начала
    def popFromHead(self):
        """Удаление элемента с начала списка"""
        if self.link_next is None:
            return self.value, None
        
        removed_value = self.value
        return removed_value, self.link_next
    
    # 6. Поиск элемента
    def search(self, value):
        """Поиск элемента по значению, возвращает индекс"""
        current = self
        index = 0
        
        while current:
            if current.value == value:
                return index
            current = current.link_next
            index += 1
        
        return -1
    
    # 7. Вставка после указанного элемента
    def insertAfter(self, target_value, new_value):
        """Вставка нового элемента после элемента с указанным значением"""
        current = self
        
        while current:
            if current.value == target_value:
                new_node = Node(new_value)
                new_node.link_next = current.link_next
                current.link_next = new_node
                return True
            current = current.link_next
        
        print(f"Элемент {target_value} не найден")
        return False
    
    # 8. Удаление указанного элемента
    def delete(self, value):
        """Удаление элемента с указанным значением"""
        # Если удаляем головной элемент
        if self.value == value:
            return self.link_next  # Возвращаем новый головной элемент
        
        current = self
        while current.link_next:
            if current.link_next.value == value:
                current.link_next = current.link_next.link_next
                return self
            current = current.link_next
        
        print(f"Элемент {value} не найден")
        return self

class Node1:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linked_list1:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.value))
            current = current.next
        return ' <-> '.join(res)
    
    def append(self, value):
        node = Node1(value)
        if not self.head:
            self.head = self.tail = node
            return
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def pop_tail(self):
        if not self.tail:
            return None
        value = self.tail.value

        if self.head == self.tail:
            self.head = self.tail = None
            return value
        
        self.tail.prev = self.tail
        self.tail.next = None
        return value



class CircularLinkedList:
    
    class CircularNode:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        res = []
        while current:
            res.append(str(current.value))
            current = current.next
            if current == self.head:
                break
        return '  ⭢ '.join(res) + f'\n⬑   {'⭠    '*(len(res)-2)}⮠'

    def append(self, value):
        node = self.CircularNode(value)
        if self.head == None:
            self.head = node
            self.head.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = node
        node.next = self.head

    def pop_tail(self):
        if not self.head:
            return None

        if self.head.next == self.head:
            value = self.head.value
            self.head = None
            return value

        current = self.head
        while current.next.next != self.head: #предпоследний
            current = current.next

        value = current.next.value
        current.next = self.head

a = CircularLinkedList()
a.append(2)
a.append(3)
a.append(4)
a.append(4)

a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.append(4)
a.append(4)
print(a.display())