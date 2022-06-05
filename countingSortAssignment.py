# Name:         Steven Tran
# OSU Email:    trans4@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment:   01 - Python Fundamentals Review
# Due Date:     2022-04-18
# Description:  Purpose is to go through review of python fundamentals learned 
# previously in CS161/162. Also to write functions under O(n) time complexity 
# using an imported Static Array class without using Python's built in list 
# class.


from enum import unique
from itertools import count
import random
from static_array import *

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    """
    Finds the minimum and maximum values of a Static Array object

    :param StaticArray arr: 1 dimensional array consisting of values

    :return tuple: (minimum, maximum)
    """
    min = arr.get(0)
    max = arr.get(0)
    for index in range(arr.length()):
        if arr.get(index) < min:
            min = arr.get(index)
        if arr.get(index) > max:
            max = arr.get(index)
    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Creates an identical array with the elements replaced with fizz, buzz, 
    or fizz buzz if divisible by 3, 5, or 15 respectively.
    
    :param StaticArray arr: static array of numeric values

    :return StaticArray:    the array with some elements replaced by strings:
                                fizz:       element is divisible by 3
                                buzz:       element is divisible by 5
                                fizzbuzz:   element is divisible by 15
    """

    length = arr.length()
    newArray = StaticArray(length)

    for index in range(length):
        if arr.get(index) % 15 == 0:
            newArray.set(index, 'fizzbuzz')
        elif arr.get(index) % 5 == 0:
            newArray.set(index, 'buzz')
        elif arr.get(index) % 3 == 0:
            newArray.set(index, 'fizz')
        else:
            newArray.set(index, arr.get(index))
    return newArray

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses the elements in a static array. Works for odd/even total number 
    of indices.

    :param StaticArray arr: a static array full of numeric values
    """
    rangelength = arr.length() // 2
    for index in range(rangelength):
        # Temporarily stores index of the first half of the array
        tempStart = arr.get(index)
        arr.set(index, arr.get(arr.length() - index - 1))
        arr.set(arr.length() - index - 1, tempStart)

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Creates an array rotated/shifted by the number of steps (positive 
    direction).

    :param StaticArray arr: a static array full of numeric values
    :param int steps: number of times to rotate the StaticArray

    :return StaticArray: a static array "rotated" by the number of steps
    """
    arrLength = arr.length()

    newArray = StaticArray(arrLength)
    for index in range(arrLength):
        jumps = (index - steps) % arrLength
        temp = arr.get(jumps)
        newArray.set(index, temp)
    return newArray

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    A static array is generated containing all the consecutive integers between
    the start and ending number (inclusive).

    :param int start:       starting value
    :param int end:         ending value

    :return StaticArray:    static array listing consecutive integers from 
                            start to end
    """
    if end > start:
        direction = 1
    elif end < start:
        direction = -1
    else:
        direction = 0
    someArray = StaticArray(abs(end - start) + 1)
    for index in range(0, someArray.length()):
        someArray[index] = start + direction * index
    return someArray


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Determines if a static array is sorted in a certain order or not.

    :param StaticArray arr: static array listing consecutive integers from 
                            start to end

    :return int:    1 : sorted in strictly ascending order (1, 2, 3, ...)
                   -1 : sorted in strictly descending order (50, 30, 10,...)
                    0 : not in any order
    """
    
    def assortment(current: int, next: int) -> int:
        """
        Compares two indices from the static array

        :param int current:     current index
        :param int next:        next index (current + 1)

        :return int:         1 : sorted in ascending order (1, 2, 3, ...)
                            -1 : sorted in descending order (50, 30, 10,...)
                             0 : not in a strict order
        """
        if arr.get(next) > arr.get(current):
            return 1
        elif arr.get(next) < arr.get(current):
            return -1
        elif arr.get(next) == arr.get(current):
            return 0
    
    # Checks condition if the static array is of length 1
    arrayLength = arr.length()
    if arrayLength == 1:
        return 1
    else:
    # compares the initial ordering with the next pair assortments
        initialOrder = assortment(0, 1)
        index = 1       # Initialize at 1 since initialOrder takes care of 
                        # the first two pairs
        while index != arrayLength - 1:
            check = assortment(index, index + 1)
            if initialOrder != check:   
                return 0
            else:
                index += 1
        return check

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple:
    """
    Finds the mode of an array.

    :param StaticArray arr: a static array consisting of elements of the same 
                            type and in order (either ascending or descending)

    :return tuple:          (highScoreValue, highScoreInstances)
    """

    # Pointer for the current element with the highest instances (mode)
    highScoreValue = None
    highScoreInstances = 0
    # Pointer for the challenging contender
    contenderValue = None
    contenderInstances = 0

    index = 0
    arrayLength = arr.length()

    while index < arrayLength:
        # 1st index = the "high score"
        if highScoreValue is None:              
            highScoreValue = arr.get(index)
            highScoreInstances += 1
        # Increases the high score's instances if the array element matches
        elif arr.get(index) == highScoreValue:  
            highScoreInstances += 1
        # Increase the contender's instances & check if it beats the current 
        # high score
        elif arr.get(index) == contenderValue:  
            contenderInstances += 1
            if contenderInstances > highScoreInstances:
                highScoreValue = contenderValue
                highScoreInstances = contenderInstances
        else:    
            # New Value is encountered that is neither the existing high score 
            # nor contender's value
            contenderValue = arr.get(index)
            contenderInstances = 1
        index += 1
    
    return (highScoreValue, highScoreInstances)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Removes any duplicate elements from an already sorted static array.

    :param StaticArray arr: a static array consisting of sorted elements

    :return StaticArray:    a static array with holding unique elements 
                            (no duplicate elements)
    """

    def getSize(array: int) -> int:
        """Determines the number of unique elements in a static array

        :param int array:   a static array consisting of sorted elements

        :return int:        # of unique elements
        """
        previous = None
        newSize = 0
        for index in range(arr.length()):
            current = arr.get(index)
            if previous is None:
                previous = current
                newSize += 1
            elif current != previous:
                previous = current
                newSize += 1
            else:
                pass
        return newSize

    def createUniqueArray(array: StaticArray, uniqueArrayLength: int) -> StaticArray:
        """
        Creates a static array consisting of no duplicate elements from the 
        original array of elements.

        :param StaticArray array:       the original static array consisting 
                                        (may contain duplicate elements)
        :param int uniqueArrayLength:   the length of the unique static array 
                                        (no duplicate elements)

        :return StaticArray:            the unique static array without any 
                                        duplicate elements
        """
        uniqueArray = StaticArray(uniqueArrayLength)
        previous = None
        uniqueSlot = 0
        for index in range(array.length()):
            current = array.get(index)
            if previous is None:
                previous = current
                uniqueArray.set(uniqueSlot, current)
                uniqueSlot += 1
            elif current != previous:
                uniqueArray.set(uniqueSlot, current)
                previous = current
                uniqueSlot += 1
            else:
                pass
        return uniqueArray
    
    uniqueSize = getSize(arr)
    uniqueArray = createUniqueArray(arr, uniqueSize)
    return uniqueArray

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    Create a copy of a static array in non-ascending order using counting sort.
    For example:
        Original:   [1, 4, 3, 5, 2]
        Sorted:     [5, 4, 3, 2, 1]

    :param StaticArray arr: orignal static array

    :return StaticArray:    static array consisting of elements from the 
                            original in non-ascending order
    """
    # Nomenclature:
    # og = original
    # counter = counting sort arithmetic
    # sorted = sorted array returned

    ogArrayLength = arr.length()

    # Determine the min and max to determine the length for the counterArray
    ogMinMax = min_max(arr)
    minimum, maximum = ogMinMax[0], ogMinMax[1]
    counterArrayLength = (ogMinMax[1] - ogMinMax[0] + 1)
    counterArray = StaticArray(counterArrayLength)
    sortedArray = StaticArray(ogArrayLength)
    
    # Initialize the counterArray values to zero
    for index in range(counterArrayLength):
        counterArray[index] = 0

    # Traverse through original array and update counts in the counter
    for index in range(ogArrayLength):
        value = arr.get(index)
        counterIndex = maximum - value
        counterData = counterArray.get(counterIndex)
        counterArray.set(counterIndex, counterData + 1)

    # Sum the counter data with the neighboring value
    for index in range(1, counterArrayLength):
        current = counterArray.get(index)
        previous = counterArray.get(index - 1)
        sum = current + previous
        counterArray.set(index, sum)

    # Rotate the indices by 1 step and update the first index to zero
    counterArray = rotate(counterArray, 1)
    counterArray.set(0, 0)

    # Traverse through the original array, and store values in the sorted array
    #  while increasing the counterIndex's value by 1 when encountered
    for index in range(ogArrayLength):
        ogValue = arr.get(index)
        counterIndex = maximum - ogValue
        sortedIndex = counterArray.get(counterIndex)
        sortedArray.set(sortedIndex, ogValue)
        counterArray.set(counterIndex, sortedIndex + 1)

    return sortedArray

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Generates a static array of all the elements within a static array, squared
    in non-descending order.

    :param StaticArray arr: a static array of numeric elements

    :return StaticArray:    a static array of the original elements squared, 
                            and sorted numerically (smallest to highest)
    """
    minAndMax = min_max(arr)
    minimum = minAndMax[0]
    maximum = minAndMax[1]
    arrLength = arr.length()
    organizedArr = StaticArray(arrLength)

    def square(input_array: StaticArray) -> StaticArray:
        """
        Squares the elements within a static array in place.

        :param StaticArray input_array: static array full of numeric elements

        :return StaticArray:            static array full of squared elements
        """
        arrLength = input_array.length()
        square_array = StaticArray(arrLength)
        for item in range(arrLength):
            square_array.set(item, input_array[item] ** 2)
        return square_array

    # Case if there are no negative values in the static array
    if minimum >= 0:
        squared = square(arr)
        return squared
    # Case if there are no positive values in the static array
    elif maximum <= 0:
        # Make a copy of the original postive array for squaring
        for item in range(arrLength):
            organizedArr.set(item, arr.get(item))
        reverse(organizedArr)
        squared = square(organizedArr)
        return squared
    # Case if there are both postive and negative elements
    else:
        neg_index = 0
        neg_length = 0
        for item in range(arrLength):
            if arr.get(item) < 0:
                neg_length += 1
        negatives = StaticArray(neg_length)
        for item in range(arrLength):
            if arr.get(item) < 0:
                negatives.set(item, arr.get(item))
        reverse(negatives)
        negatives = square(negatives)

        # Create a static array of just the positive elements
        pos_length = arrLength - neg_length
        positives = StaticArray(pos_length)

        pos_index = 0
        for item in range(neg_length, arrLength):
            positives.set(pos_index, arr.get(item))
            pos_index += 1
        positives = square(positives)

    # Add the smallest data element from positves or negatives array to the 
    # organized array
    neg_index = 0
    pos_index = 0
    org_index = 0       
    
    while (neg_index < neg_length) or (pos_index < pos_length):
        if neg_index == neg_length:
            organizedArr.set(org_index, positives.get(pos_index))
            pos_index += 1
            org_index += 1
        elif pos_index == pos_length:
            organizedArr.set(org_index, negatives.get(neg_index))
            neg_index += 1
            org_index += 1
        elif negatives.get(neg_index) <= positives.get(pos_index):
            organizedArr.set(org_index, negatives.get(neg_index))
            neg_index += 1
            org_index += 1
        else:
            organizedArr.set(org_index, positives.get(pos_index))
            pos_index += 1
            org_index += 1
        
    return(organizedArr)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
