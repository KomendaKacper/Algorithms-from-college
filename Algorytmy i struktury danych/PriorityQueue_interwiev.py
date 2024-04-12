import sys

class Element():
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
    
    def __str__(self):
        return str(self.value) + " " + str(self.priority)

class PriorityQueue():
    def __init__(self, size):
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

    def enqueue(self, value, priority):
        if self.is_full() == True:
            lowest_priority = priority
            lowest_id = None
            for i, e in enumerate (self.prioqueue):
                if e.priority < lowest_priority:
                    lowest_priority = e.priority
                    lowest_id = i
                
            if lowest_id is not None:
                self.prioqueue[i] = None
            
        for i, e in enumerate(self.prioqueue):
            if e is None:
                self.prioqueue[i] = Element(value, priority)
                break
            elif e.priority < priority:
                self.prioqueue[i+1:] = self.prioqueue[i:-1]
                self.prioqueue[i] = Element(value, priority)
                break
            elif e.priority == priority:
                self.prioqueue[i+2:] = self.prioqueue[i+1:-1]
                self.prioqueue[i+1] = Element(value, priority)
                break
    
    def dequeue(self):
        for i in range (len(self.prioqueue)):
            if self.prioqueue is None:
                return None
            else:
                self.prioqueue[i:] = self.prioqueue[i+1:] + [None]
                break


# for line in sys.stdin: 
#     tokens = line.split()
#     if tokens[0] == "enqueue":
#         value = int(tokens[1])
#         priority = int(tokens[2])
#         queue.enqueue(value, priority)
#     elif tokens[0] == "dequeue":
#         queue.dequeue()
#     else:
#         queue = PriorityQueue(int(tokens[0]))
# print (queue)
