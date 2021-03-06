class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

    def getData(self):
        return (self.data)

    def setData(self,value):
        self.data = value

    def getNext(self):
        return (self.next)

    def setNext(self,newnext):
        self.next = newnext

class linkedlist():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current!= None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        found = False
        current = self.head
        while found == False and current!= None:
            if current.getData() == item:
                found = True
            current = current.getNext()
        return found

    def remove(self,item):
        found = False
        current = self.head
        prev = None
        while found == False and current != None:
            if current.getData() == item:
                found = True
            else:
                prev = current
                current = current.getNext()

        if found==True:
            if prev==None:
                self.head = current.getNext()
            else:
                prev.setNext(current.getNext())





ll = linkedlist()
ll.add(5)
ll.add(9)

ll.remove(9)
ll.remove(5)
print(ll.size())