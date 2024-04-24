import random
import time

class Element:
    def __init__(self, priority, data):
        self.__value = data
        self.__priority = priority
    
    def __repr__(self):
        return repr(self.__priority) + " : " + repr(self.__value)
    
    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority

class PriorityQueue:
    def __init__(self, lista=None):
        if lista is not None:
            self.prioqueue = lista
        else:
            self.prioqueue = []
        self.size = len(self.prioqueue)
        self.heap()
  
    def is_empty(self):
        return self.size == 0
  
    def peek(self):
        if self.is_empty():
            return None
        return self.prioqueue[0]
  
    def heap(self):
        i = self.parent(self.size - 1)
        while i >= 0:
            self.sort_heap(i)
            i -= 1
        return self.prioqueue
  
    def heap_sort(self):
        s = self.size

        while s > 0:
            self.dequeue()
            s -= 1
        return self.prioqueue
  
    def sort_heap(self, node=0):
        while True:
            left = self.left(node)
            right = self.right(node)
            parent = node
      
            if left < self.size and self.prioqueue[left] > self.prioqueue[parent]:
                parent = left
            if right < self.size and self.prioqueue[right] > self.prioqueue[parent]:
                parent = right 
        
            if parent != node:
                self.prioqueue[node], self.prioqueue[parent] = self.prioqueue[parent], self.prioqueue[node]
                node = parent
            else:
                break
    
    def dequeue(self):
        if self.is_empty():
            return None
        self.size -= 1
        self.prioqueue[0], self.prioqueue[self.size] = self.prioqueue[self.size], self.prioqueue[0]
        self.sort_heap(0)
        return self.prioqueue[self.size]
  
    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2
  
    def print_dict(self):
        print("{", end=" ")
        for i in range(self.size):
            if self.prioqueue[i] is not None:
                print(self.prioqueue[i], end=", ")
        print("}")
    
    def print_tree(self, idx = 0, lvl= 0):
        if idx < len(self.prioqueue):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.prioqueue[idx] if self.prioqueue[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

def swap(lista):
    n = len(lista)
    for i in range(n):
        min_val = lista[i]
        for j in range(i, n):
            if min_val > lista[j]:
                lista[j], lista[i] = lista[i], lista[j]
                min_val = lista[j]
    return lista
    
def shift(lista):
    n = len(lista)
    for i in range(n):
        min_val = lista[i]
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < min_val:
                min_val = lista[j]
                min_idx = j
        if min_idx != i:
            m = lista.pop(min_idx)
            lista.insert(i, m)
    return lista

def main():
    lista = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    nodes = [Element(k, v) for k, v in lista]
    heap = PriorityQueue(nodes)
    print ("Lista nieposortowana:")
    heap.print_dict()
    print ()
    print ("Lista jako drzewo:")
    heap.print_tree()
    print ()
    heap_sorted = heap.heap_sort()
    print ()
    print ("Posortowane za pomocą heapsort: ")
    print(heap_sorted)
    print("Algorytm nie jest stabilny")

    lista = [random.randint(0, 99) for _ in range(10000)]
    priorityqueue = PriorityQueue(lista)
    t_start = time.perf_counter()
    priorityqueue.heap_sort()
    t_stop = time.perf_counter()
    print("Zmierzony czas dla heap_sort:", "{:.7f}".format(t_stop - t_start))
    print ()
#---------------------------------------------------------------------------------------------

    lista = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    nodes = [Element(k, v) for k, v in lista]
    print("Posortowane zaz pomocą swap:")
    print (swap(nodes))
    print("Algorytm nie jest stabilny")
    
    lista = [random.randint(0, 99) for _ in range(10000)]
    t_start = time.perf_counter()
    swap(lista)
    t_stop = time.perf_counter()
    print("Zmierzony czas dla swap:", "{:.7f}".format(t_stop - t_start))
    print ()
    

    lista = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    nodes = [Element(k, v) for k, v in lista]
    print ("Posortowane za pomocą shift:")
    print (shift(nodes))
    print("Algorytm jest stabilny")

    lista = [random.randint(0, 99) for _ in range(10000)]
    t_start = time.perf_counter()
    shift(lista)
    t_stop = time.perf_counter()
    print("Zmierzony czas dla shift:", "{:.7f}".format(t_stop - t_start))
  
if __name__ == "__main__":
    main()
