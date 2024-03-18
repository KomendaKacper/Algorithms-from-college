class CircularQueue():
    def __init__(self, size = 5):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.rear == self.front
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            print(self.queue[self.front])
        
    def enqueue(self, arg):
        self.queue[self.rear] = arg
        self.rear = (self.rear + 1) % self.size
        
        if (self.rear) % self.size == self.front:
            self.queue = self.realloc()

    def dequeue(self):
        if self.is_empty():
            print ("Tablica jest pusta")
        else:
            x = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            print (x)

    def __str__(self):
        if self.is_empty():
            return '[]'
        else:
            return str(self.queue)

    def realloc(self):
        oldSize = len(self.queue)
        if self.rear == 0:
            self.rear = oldSize
            self.size *= 2
            return [self.queue[i] if i < oldSize else None for i in range(oldSize*2)]
        else:
            new_matrix = [None for i in range (oldSize*2)]
            for i in range (self.rear):
                new_matrix[i] = self.queue[i]
            for i in range (oldSize+self.rear, oldSize*2):
                new_matrix[i] = self.queue[i-oldSize]
            self.front += self.size
            self.size *= 2
            return new_matrix


def main():
    queue = CircularQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.peek()
    print (queue)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    print (queue)
    while queue.is_empty() == False:
        queue.dequeue()
    print (queue)
    
if __name__ == "__main__":
    main()
    