from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0

    def __str__(self):
        list_a = []
        current = self.head
        while current is not None:
            list_a.append(current.data)
            current = current.next
        print (list_a)

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def add(self, data):
        node = Node(ndata)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.n += 1

    def remove(self, ndata):
        current = self.head
        previous = None
        found = False
        while current is not None:
            if current.data == ndata:
                found = True
                break
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = self.head.next
            else:
                previous.next = current.next
                current.next = None
            self.n -= 1
        return found

    def size(self):
        return self.n

    def isEmtpy(self):
        return self.n == 0
