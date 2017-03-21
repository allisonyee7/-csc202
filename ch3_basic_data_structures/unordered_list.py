from node import Node

class UnorderedList:
    def ___init___(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while not (current is None):
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while not (current is None):
            if current.getItem() == data:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getItem() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            prev.setNext(current.getNext())
