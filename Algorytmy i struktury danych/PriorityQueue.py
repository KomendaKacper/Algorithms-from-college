#Niedokończone

class Element():
    def __init__(self, priority, value):
        self.__value = value
        self.__priority = priority
    
    def __repr__(self):
        return repr(self.__priority) + " " + repr(self.__value)
    
    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority
    
    def __eq__(self, other):
        return self.__priority == other.__priority

class PriorityQueue():
    def __init__(self, size):
        self.size = size
        self.prioqueue = [None for _ in range(size)]
        
    def __str__(self):
        s = ""
        for e in self.prioqueue:
            if e is not None:
                s += str(e) + "\n"
            else:
                pass
        if s != "":
            return s[:-1]
        else:
            return "Empty"
    
    def is_full(self):
        for e in self.prioqueue:
            if e is None:
                return False
        return True
    
    def is_empty(self):
        for e in self.prioqueue:
            if e is not None:
                return False
        return True

    def enqueue(self, element):
        if self.is_full() == True:
            self.prioqueue()
            
        for i, e in enumerate(self.prioqueue):
            if e is None:
                self.prioqueue[i] = element
                break
            elif e < element:
                self.prioqueue[i+1:] = self.prioqueue[i:-1]
                self.prioqueue[i] = element
                break
            elif e == element:
                self.prioqueue[i+2:] = self.prioqueue[i+1:-1]
                self.prioqueue[i+1] = element
                break
    
    def dequeue(self):
        if self.is_empty():
            print (None)
            return None
        else:
            print (self.prioqueue[0])
            self.prioqueue = self.prioqueue[1:] + [None]
            
    
    def peek(self):
        return self.prioqueue[0]
    
    def left(self, index):
        if index == 0:
            return self.prioqueue[1]
        else:
            return self.prioqueue[2 * index]
    
    def right(self, index):
        if index == 0:
            return self.prioqueue[2]
        else:
            return self.prioqueue[(2*index) + 1]

    # def parent(self, index):


queue = PriorityQueue(5)
element1 = Element(4,5)
# element2 = Element(6,10)
queue.enqueue(element1)
# queue.enqueue(element2)
# queue.enqueue(Element(3,25))
print (queue)
print (queue.left(0))
print (queue.right(0))

