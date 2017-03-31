def readInput():
    print ("Enter list:")
    data = input()
    data = data.strip()
    data = data.split(" ")
    return data


def reverseList(nlist):
    if len(nlist) == 1:
        return nlist
    revList = reverseList(nlist[1:])
    revList.append(nlist[0])
    return revList


def main():
    nlist = readInput()
    result = reverseList(nlist)
    print ("Reversed list: ", result)


if __name__ == '__main__':
    main()
