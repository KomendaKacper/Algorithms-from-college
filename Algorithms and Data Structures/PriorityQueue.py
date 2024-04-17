class Element:
    def __init__(self, priority, value):
        self.__value = value
        self.__priority = priority
    
    def __repr__(self):
        return repr(self.__priority) + " : " + repr(self.__value)
    
    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority

class PriorityQueue:
    def __init__(self):
        self.prioqueue = []

    def __str__(self):
        s = "{"
        for e in self.prioqueue:
            if e is not None:
                s += str(e) + ", "
        if s != "{":
            s = s[:-2]
        s += "}"
        return s

    def is_empty(self):
        return len(self.prioqueue) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.prioqueue[0]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            res = self.prioqueue[0]
            self.prioqueue[0] = self.prioqueue[-1]
            self.prioqueue.pop()
            self.sort_heap(0)
            return res

    def enqueue(self, element):
        self.prioqueue.append(element)
        index = len(self.prioqueue) - 1
        while index > 0 and self.prioqueue[index] > self.prioqueue[self.parent(index)]:
            parent = self.parent(index)
            self.prioqueue[index], self.prioqueue[parent] = self.prioqueue[parent], self.prioqueue[index]
            index = parent

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def sort_heap(self, node):
        left_child = self.left(node)
        right_child = self.right(node)
        max_node = node

        if left_child < len(self.prioqueue) and self.prioqueue[left_child] > self.prioqueue[max_node]:
            max_node = left_child
        if right_child < len(self.prioqueue) and self.prioqueue[right_child] > self.prioqueue[max_node]:
            max_node = right_child

        if max_node != node:
            self.prioqueue[node], self.prioqueue[max_node] = self.prioqueue[max_node], self.prioqueue[node]
            self.sort_heap(max_node)

    def print_dict(self):
        print("{", end=" ")
        for e in self.prioqueue:
            if e is not None:
                print(e, end=", ")
        print("}")

    def print_tree(self, idx, lvl):
        if idx < len(self.prioqueue):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.prioqueue[idx] if self.prioqueue[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)


if __name__ == "__main__":
    kolejka = PriorityQueue()
    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    wartości = "GRYMOTYLA"
    
    for priorytet, wartość in zip(priorytety, wartości):
        kolejka.enqueue(Element(priorytet, wartość))

    print("Kolejka jako drzewo:")
    kolejka.print_tree(0, 0)

    print("Kolejka jako tablica:")
    print(kolejka)

    pierwsza_dana = kolejka.dequeue()

    kolejna_dana = kolejka.peek()
    print("Następna dana:", kolejna_dana)

    print("Kolejka jako tablica:")
    print(kolejka)

    print("Usunięta pierwsza dana:", pierwsza_dana)

    print("Opróżnianie kolejki:")
    while not kolejka.is_empty():
        print(kolejka.dequeue())

    print("Opróżniona kolejka:")
    print(kolejka)
