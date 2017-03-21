class OrderedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        a = []
        current = self.head
        while current is not None:
            a.append(curr.data)
            current = current.next
        print (a)

    def isEmpty(self):
        return self.head is None

    def popPos(self, key):
        if self.isEmpty():
            return False
        front = self.head
        previous = None
        count = 0
        node = None
        found = False
        while front is not None:
            if count == key:
                found = True
                break
            count += 1
            prev = front
            front = front.next
        if not found:
            return node

        if previous is None:
            node = self.head
            self.head = self.head.next
        else:
            node = front
            previous.next = front.next
            front.next = None
        return node

    def pop(self):
        if self.isEmpty():
            return None

        if self.head.next is None:
            node = self.head
            self.head = None
            return node

        front = self.head
        back = None
        while front.next is not None:
            back = front
            front = front.next
        node = front
        back.next = front.next
        return node

    def search(self, key):
        if self.isEmpty():
            return -1
        current = self.head
        index = 0

        while not (current is None):
            if current.getData() == key:
                return index
            elif key < current.getData():
                break
            current = current.getNext()
            index += 1
        return -1

    def size(self):
        current = self.head
        count = 0
        while not (current is None):
            count += 1
            current = current.getNext()
        return count

    def add(self, item):
        current = self.head
        previous = None
        while not (current is None):
            if current.getItem() > item:
                break
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if prev is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            prev.setNext(temp)

    def remove(self, item):
        if self.isEmpty():
            return None
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getItem() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        node = None
        if previous is None:
            node = self.head
            self.head = current.getItem()
        else:
            node = current
            previous.setNext(current.getNext())
        return node
