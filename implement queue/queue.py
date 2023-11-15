class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_item = queueNode(data)
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item

    def pop(self):
        if self.head is None:
            return None
        item = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return item

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        string = ""
        item = self.head
        while item:
            string += "{} => ".format(item.data)
            item = item.next
        return string + "None"

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


class queueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    queue = Queue()
    queue.insert(5)
    queue.insert(10)
    queue.insert(20)
    print(queue.pop())
    print(queue)
    print(queue.isEmpty())
    print(queue.pop())
    print(queue)
    print(queue.isEmpty())
    queue.insert(50)
    queue.pop()
    print(queue.size())
