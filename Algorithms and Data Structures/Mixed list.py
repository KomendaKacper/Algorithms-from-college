class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)



class Table:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.tab = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2
    
    def search(self, key):
        for e in self.tab:
            if e == None:
                pass
            else:
                if e.key == key:
                    print (e.value)
                    return
        print ("Nie ma elementu o takim kluczu")

    def insert(self, key, value):
        if type(value) == str:
            suma = 0
            for e in value:
                suma += ord(e)
            value = suma
        
        if type(key) == str:
            suma = 0
            for e in key:
                suma += ord(e)
            key = suma
        
        el = Element(key, value)
        k = el.key%len(self.tab)
        i = 0
        l = len(self.tab)
        if self.tab[k] == None:
            self.tab[k] = el
        elif self.tab[k].key == key:
            self.tab[k%len(self.tab)] = el
        else:
            while self.tab[k] != None:
                if l + 1 == i:
                    break
                k = (el.key%len(self.tab) + self.c1*i + self.c2*i**2)%len(self.tab)
                i += 1
            if l + 1 == i:
                print ("Brak miejsca")
            else:
                self.tab[k] = el
        
    
    def remove(self, key):
        k = key%len(self.tab) 

        self.tab[k] = None

    def __str__(self):
            result = "{"
            for e in self.tab:
                if e is None:
                    result += "None" + ", "
                else:
                    result += str(e)+ ", "
            result = result[:-2] + "}"
            return result

def test1(size=13, c1=1, c2=0):
    tab = Table(size, c1, c2)
    tab.insert(0,"A")
    tab.insert(1,"B")
    tab.insert(2,"C")
    tab.insert(3,"D")
    tab.insert(4,"E")
    tab.insert(5,"F")
    tab.insert(18,"G")
    tab.insert(31,"H")
    tab.insert(8,"I")
    tab.insert(9,"J")
    tab.insert(10,"K")
    tab.insert(11,"L")
    tab.insert(12,"M")
    tab.insert(13,"N")
    tab.insert(14,"O")
    print (tab)
    tab.search(5)
    tab.search(14)
    tab.insert(5,"Z")
    tab.search(5)
    tab.remove(5)
    print (tab)
    tab.search(31)
    tab.insert("test", "W")

def test2(size = 13, c1 = 1, c2 = 0):
    tab = Table(size, c1, c2)
    tab.insert(13,"A")
    tab.insert(26,"B")
    tab.insert(39,"C")
    tab.insert(52,"D")
    tab.insert(65,"E")
    tab.insert(78,"F")
    tab.insert(91,"G")
    tab.insert(104,"H")
    tab.insert(117,"I")
    tab.insert(130,"J")
    tab.insert(143,"K")
    tab.insert(156,"L")
    tab.insert(169,"M")
    print (tab)

test1()
test2()
test2(13, 0, 1)
test1(13, 0, 1)
