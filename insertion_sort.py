def insertion_sort(someList):
    if len(someList) < 2:
        return someList
    for i in range(1, len(someList)):
        current = someList[i]

        leftIndex = i - 1
        # Ensuring we check only valid indices >= 0, and the current value is less than its left(s)
        while leftIndex >= 0 and current < someList[leftIndex]:
            someList[leftIndex + 1] = someList[leftIndex]
            leftIndex -= 1
        someList[leftIndex + 1] = current
    
    return someList

def main():
    woot = [5, 12, 3, 19, 200, 0]
    print(insertion_sort(woot))

    animals = ['donkey', 'walrus', 'moose', 'caboose', 'llama', 'ant', 'bull']
    print(insertion_sort(animals))

    nada = ['donkey', 'aaaa']
    print(insertion_sort(nada))

if __name__ == "__main__":
    main()
