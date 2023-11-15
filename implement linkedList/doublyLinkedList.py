class doublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def insertAfter(self, data, new):
        if (self == None): return
        item = self
        newItem = doublyLinkedList(new)
        while (item):
            if (item.data == data):
                break
            item = item.next
        newItem.prev = item
        newItem.next = item.next
        item.next = newItem
    def insertBefore(self, data , new):
        newItem = doublyLinkedList(data)
        item = self
        if (item.data == data):
            newItem.next = item.next
            newItem.prev = item
            item.data = new
            item.next = newItem
            return
        while(item):
            if (item.next.data == data):
                break
            item = item.next
        newItem.data = new
        newItem.prev = item
        newItem.next = item.next
        item.next = newItem
    def deleteNode(self, data):
        if (self == None): return
        if (self.data == data):
            self.data = self.next.data
            self.next = self.next.next
            return
        item = self
        while (item):
            if (item.next.data == data):
                break
            item = item.next
        if (item.next.next == None):
            item.next = None
            return
        temp = item.next.next
        item.next = temp
        temp.prev = item
    def insertLast(self, new):
        newItem = doublyLinkedList(new)
        item = self
        while(item.next):
            item = item.next
        newItem.prev = item
        item.next = newItem
    def __str__(self):
        string = ""
        item = self
        while (item):
            string += "{} -> ".format(item.data)
            item = item.next
        string += "done"
        return (string)
if __name__ == "__main__":
    part = doublyLinkedList(10)
    part.insertAfter(10, 20)
    part.insertAfter(10, 30)
    part.insertAfter(20, 50)
    part.insertBefore(50, 15)
    part.insertBefore(10, 5)
    part.deleteNode(5)
    part.deleteNode(10)
    part.deleteNode(50)
    part.insertLast(133)
    print(part)
        
