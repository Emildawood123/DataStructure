class Stack:
    def __init__(self, head=None, tail=None):
        if ((head and tail) or not (head and tail)):
            self.head = head
            self.head.next = tail
            self.tail = tail
        elif (head):
            self.head = head
            self.tail = head
        else:
            self.head = tail
            self.tail = tail
    def insert(self, data):
        newItem = StackNode(data)
        if (self.head is None):
            self.head = newItem
            self.tail = newItem
        elif (self.head == self.tail):
            self.head.next = newItem
            self.tail = newItem
        else:
            self.tail.next = newItem
            self.tail = newItem
    def pop(self):
        item = self.tail.data
        if (self.head.data == self.tail.data):
            self.head.data = self.tail.data = None
            return item
        temp = self.head
        while (temp):
            if (temp.next == self.tail):
                break
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        return item
    def peek(self):
        return self.head.data
    def isEmpty(self):
        if (self.head.data == None):
            return "your stack is empty"
        else: return "your stack have elements or one element"
    def __str__(self):
        string = ""
        item = self.head
        while(item):
            string += "{} => ".format(item.data)
            item = item.next
        return string
    def size(self):
        if (Stack.isEmpty(self) == "your stack is empty"):
            return 0
        temp = self.head
        count =0
        while (temp):
            count += 1
            temp = temp.next
        return count


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":
    stack = Stack(StackNode(5), StackNode(10))
    stack.insert(20)
    print(stack.pop())
    print(stack)
    print(stack.isEmpty())
    print(stack.pop())
    print(stack)
    print(stack)
    print(stack.isEmpty())
    stack.insert(50)
    stack.pop()
    print(stack.size())
    stack.pop()
    print(stack.size())
