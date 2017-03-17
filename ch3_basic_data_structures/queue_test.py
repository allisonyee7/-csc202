from queue_adt import Queue

def testQueue():
    x = Queue()
    x.enqueue('hi')
    x.enqueue('blah')
    x.enqueue('bleh')
    x.enqueue(4)
    print("Dequeue: ", x.dequeue())
    while not x.is_empty():
        print(x.dequeue())

def main():
    testQueue()

if __name__ == '__main__':
    main()

