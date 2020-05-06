class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def getNext(self):
        return self.next

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self,item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() == item:
                previous.setNext(current.getNext())
                

mylist = UnorderedList()
mylist.add(1)




# for x in mylist:
#     print(x)

# first = Node('a')
# first.next = Node('b')
# first.next.next = Node('c')
#
# print(first.next.next.data)
