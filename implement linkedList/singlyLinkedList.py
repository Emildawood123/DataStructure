class linkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def insert(self, data):
        new = linkedList(data)
        item = self
        while (item.next):
            item = item.next
        item.next = new
    def __str__(self):
        item = self
        strint = ""
        while (item):
            strint +=  " " + str(item.data) + " next - > "
            item = item.next
        strint += "NULL"
        return strint
    def getLength(self):
        if (self is None):
            return 0
        item = self
        count = 0
        while (item):
            item = item.next
            count +=1
        return count
    def insertAfter(self, number, new):
        item = self
        newItem = linkedList(new)
        while (item):
            if (item.data == number):
                break
            item = item.next
        if (item is None):
            raise Exception("not found")
        if (item.next):
            newItem.next = item.next
            item.next = newItem
        else:
            item.next = newItem
    def deleteNode(self, data):
        item = self
        newItem = self.next
        if (type(data) == int):
            print("good")
            if (item.data == data):
                self.data = newItem.data
                self.next = newItem.next
                return
            while (item):
                if (item.next.data == data):
                    break
                item = item.next
            if (item.next.next):
                item.next = item.next.next
            else:
                item.next = None
        else:
            if (item == data):
                self.data = newItem.data
                self.next = newItem.next
                return
            while (item):
                if (item.next == data):
                    break
                item = item.next
            if (item.next.next):
                item.next = item.next.next
            else:
                item.next = None
    def insertBefore(self, number, new):
        item = self
        newItem = linkedList(number)
        newItem.next = self.next
        if (item.data == number):
            self.data = new
            self.next = newItem
            return
        while (item):
            if (item.next is None):
                raise Exception("not found")
            if (item.next.data == number):
                break
            item = item.next
        newItem.data = new
        newItem.next = item.next
        item.next = newItem

    def findParent(self, data):
        item = self
        if (self.data == data):
            return (" {}: the head has no parent".format(self.__dict__))
        while (item):
            if (item.next is None):
                raise Exception("not found the child")
            if (item.next.data == data):
                return item.data
            item = item.next


if __name__ == "__main__":
    a = linkedList(5)
    a.insert(20)
    a.insert(15)
    a.insert(80)
    a.insertAfter(80, 10)
    a.deleteNode(10)
    a.deleteNode(15)
    a.deleteNode(5)
    a.insertBefore(20, 5)
    a.insertBefore(20, 4)
    a.insertBefore(80, 30)
    print(a.findParent(5))
    len = a.getLength()
    print(a)
    print(len)
