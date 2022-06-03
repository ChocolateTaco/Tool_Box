def selectionSort(someList: list) -> None:
    """
    Implements selection sort on the list of items. O(n^2)

    :param list someList: a list object
    """

    for element in range(len(someList)):
        currentLowestIndex = element
        for compared in range(element + 1, len(someList)):
            if someList[compared] < someList[currentLowestIndex]:
                currentLowestIndex = compared
        # If the starting index found a lower value
        if currentLowestIndex != element:
            someList[element], someList[currentLowestIndex] = someList[currentLowestIndex], someList[element] 

    return someList

woot = [5, 12, 3, 19, 200, 0]
print(selectionSort(woot))

animals = ['donkey', 'walrus', 'moose', 'caboose', 'llama', 'ant', 'bull']
print(selectionSort(animals))