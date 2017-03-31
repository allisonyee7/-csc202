import time


def readInput():
    while True:
        num = input("Enter fibonacci number:  ")
        num = num.strip()
        if not num.isdigit():
            print ("Enter an integer: ")
            continue
        num = int(num)
        if num < 0:
            print ("Enter a positive integer: ")
            continue
        return num


def fibonacci_iter(num):
    if num == 0 or num == 1:
        return num
    fib1 = 0
    fib2 = 1
    count = 2
    result = 1
    while count <= num:
        result = fib1 + fib2
        fib1, fib2 = fib2, result
        count += 1
    return result


def fibonacci_rec(num):
    if num <= 2:
        return 1
    return fibonacci_rec(num-1) + fibonacci_rec(num-2)


def main():
    num = readInput()
    start = time.clock()
    result = fibonacci_iter(num)
    end = time.clock()
    print("Fibonacci number %d is: %d in time(iterative): %f" %
          (num, result, round((end - start), 5)))
    start = time.clock()
    result = fibonacci_rec(num)
    end = time.clock()
    print("Fibonacci number %d is: %d in time(recursively): %f" %
          (num, result, round((end - start), 5)))


if __name__ == '__main__':
    main()
