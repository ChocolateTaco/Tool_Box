def shellSort(someList):
    elements = len(someList)
    gap = elements//2

    while gap > 0:
        for i in range(gap, elements):
            # The current value
            temp = someList[i]
            j = i - gap

            # Checking the left value with the current value until we reach the end of the list. Swap them if the left value(s) are greater than the current value on the list (righter value)
            while(j>=0 and someList[j] > temp):
                someList[j + gap] = someList[j]
                j = j - gap
            someList[j + gap] = temp
        gap = gap // 2
    
    return someList

def main():
    woot = [5, 12, 3, 19, 200, 0]
    print(shellSort(woot))

    animals = ['donkey', 'walrus', 'moose', 'caboose', 'llama', 'ant', 'bull']
    print(shellSort(animals))

    nada = ['donkey', 'aaaa']
    print(shellSort(nada))

if __name__ == "__main__":
    main()