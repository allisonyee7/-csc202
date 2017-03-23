from queue_adt import Queue

def radix_sort(n):
    if n is None or len(n)<10:
        return n 
    main_q = Queue()
    bin_q = []

    for n in nums:
        main_q.enqueue(n)

    for i in range(10):
        bin_q.append(Queue())

    maxLength = len(nums[0])
    for i in range(1, len(n)):
        if len(n[i]) > maxLength:
            maxLength =len(n[i])

    for i in range(1, maxLength + 1):
        visited = []
        while not main_q.is_empty():
            v = main_q.dequeue()
            if i > len(v):
                visited.append(v)
                continue
            r = v[-i]
            r = int(r)
            bin_q[r].enqueue(v)
        for v1 in visited:
            main_q.enqueue(v1)
        for i in range(10):
            while not bin_q[i].is_empty():
                main_q.enqueue(bin_q[i].dequeue())
    result = []
    while not main_q.is_empty():
        result.append(main_q.dequeue())
    return result 





if __name__ == '__main__':
    main()

