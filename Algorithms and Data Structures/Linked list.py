#Niedokonczone
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
    
class ListNode:
    def __init__(self):
        self.head = None
        
    def destroy(self):
        self.head = None
    
    def add(self, arg):
        if self.head is None:
            self.head = Node(arg)
        else:
            temp = Node(arg, self.head)
            self.head = temp

    def append(self, arg):
        if self.head == None:
            self.head = Node(arg)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(arg) 
        
    def display(self):
        cur = self.head
        list = []
        if cur == None:
            print (list)
        else:
            while cur:
                list.append(cur.data)
                cur = cur.next
            for node in list:
                print ("-> ", end = "")
                print (node.data)

    def remove(self):
        cur = self.head
        if cur == None:
            print("Pusta lista!")
        else:
            self.head = cur.next

    def remove_end(self):
        cur = self.head
        if cur == None:
            print("Pusta lista!")
        elif cur.next == None:
            self.head = None
        else:
            while cur.next.next:
                cur = cur.next
            cur.next = None

    def length(self):
        cur = self.head
        i = 0
        while cur:
            i += 1
            cur = cur.next
        return i

    def is_empty(self):
        return self.head == None
            
    def get(self):
        return self.head
        
def main():
    list = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]
    node0 = Node(list[0])
    node1 = Node(list[1])
    node2 = Node(list[2])
    node3 = Node(list[3])
    node4 = Node(list[4])
    node5 = Node(list[5])
    uczelnie = ListNode()
    uczelnie.append(node0)
    uczelnie.append(node1)
    uczelnie.append(node2)
    uczelnie.add(node3)
    uczelnie.add(node4)
    uczelnie.add(node5)
    print ("Pełna lista to: ")
    uczelnie.display()
    print ("Dlugosc listy wynosi: ",uczelnie.length())
    uczelnie.remove()
    print("Pierwszy element po usunieciu pierwszego elementu to: ")
    print (uczelnie.get())
    uczelnie.remove_end()
    print ("Lista po usunieciu ostatniego elementu to: ")
    uczelnie.display()
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(node0)
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == "__main__":
    main()