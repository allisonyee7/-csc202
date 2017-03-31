def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


def f_input():
    while True:
        num = input("Enter number: ")
        num = num.strip()
        if num.isdigit():
            num = int(num)
            return num
        else:
            print("Put another input")

def main():
    num = f_input()
    fact = factorial(num)
    print ("Factorial of %d is: %d" % (num, fact))

if __name__ == '__main__':
    main()
