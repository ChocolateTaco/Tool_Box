
def merging(list1, list2):
    """
    Merges two sorted lists with one another

    :param _type_ list1: a sorted list object
    :param _type_ list2: a sorted list object
    """
    if len(list1) == 0 or len(list2) == 0:
        return
    p1, p2 = 0, 0
    newList = []

    # When there are elements still in both lists
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            newList.append(list1[p1])
            p1 += 1
        else:
            newList.append(list2[p2])
            p2 += 1

    # When one of the list runs out of elements, dump the remaining
    while p1 < len(list1) or p2 < len(list2):
        if p1 < len(list1):
            newList.append(list1[p1])
            p1 += 1
        else:
            newList.append(list2[p2])
            p2 += 2
    
    return newList

def singleMerge(array, left, mid, right):
    p1 = left
    p2 = mid + 1
    tempArray = []
    while p1 <= mid and p2 <= right:
        if array[p1] <= array[p2]:
            tempArray.append(array[p1])
            p1 += 1
        else:
            tempArray.append(array[p2])
            p1 += 2
    
    while p1 <= mid or p2 <= right:
        if p1 <= mid:
            tempArray.append(array[p1])
            p1 += 1
        else:
            tempArray.append(array[p2])
            p2 += 1
    array = tempArray

def mergeSort(someList):
    """
    Sorts a list recursively via divide and conquer

    :param _type_ someList: an unsorted list object
    """

    if len(someList) > 1:
        mid = len(someList) // 2
        left = someList[:mid]
        right = someList[mid:]
        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                someList[k] = left[i]
                i += 1
            else:
                someList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            someList[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            someList[k] = right[j]
            j += 1
            k += 1

def main():
    someList1 = [3, 20, 30, 40, 50]
    someList2 = [6, 25, 35, 45, 55]
    print(merging(someList1, someList2))

    scrambled = [8, 2, 9, 6, 5, 3, 7, 4]
    print(mergeSort(scrambled))
    print(scrambled)


if __name__ == "__main__":
    main()