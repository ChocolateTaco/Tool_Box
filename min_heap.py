# Name:             Steven Tran
# OSU Email:        trans4@oregonstate.edu
# Course:           CS261 - Data Structures
# Assignment:       Assignment 5
# Due Date:         2022-05-23
# Description:      Implementation of the Minimum Heap data structure.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds a node to a minimum heap

        :param object node:     an object such as an int, string, or float
        """
        if self.is_empty():
            self._heap.append(node)
        else:
            nodeIndex = self._heap.length()
            self._heap.append(node)
            parentIndex = (nodeIndex - 1)//2   
            parentVal = self._heap.get_at_index(parentIndex)
            while node < parentVal:
                self._heap.set_at_index(nodeIndex, parentVal)
                self._heap.set_at_index(parentIndex, node)
                nodeIndex = parentIndex
                parentIndex = (nodeIndex - 1)//2       
                if parentIndex < 0:
                    break
                parentVal = self._heap.get_at_index(parentIndex)


    def is_empty(self) -> bool:
        """
        Determines if the heap is empty.

        :return bool:       True:   is empty
                            False:  heap has at least 1 node
        """
        return self._heap.is_empty()


    def get_min(self) -> object:
        """
        Determines the minimum/smallest node in the heap.

        :raises MinHeapException:   Error raised if heap is empty

        :return object:             Smallest value in the heap
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Retrieves and removes the smallest node in the heap.

        :raises MinHeapException:   Error raised if heap is empty

        :return object:             Smallest value in the heap
        """
        if self.is_empty():
            raise MinHeapException
        else:
            minValue = self.get_min()
            lastValue = self._heap.pop()
            # Store the last occupied node to the top of the heap & perc down
            if self._heap.length() > 0:
                self._heap.set_at_index(0, lastValue)
                _percolate_down(self._heap, 0)
            return minValue

    def build_heap(self, da: DynamicArray) -> None:
        """
        Creates a new minimum heap from a dynamic array.

        :param DynamicArray da: a dynamic array object
        """
        self.clear()
        for element in range(da.length()):                  # O(n)
            self._heap.append(da.get_at_index(element))     # amortized(1)
        lastNonLeaf = self._heap.length() // 2 - 1          # O(1)
        for nonLeaf in range(lastNonLeaf, -1, -1):          # O(log(n))
            _percolate_down(self._heap, nonLeaf)            # O(log(n))

    def size(self) -> int:
        """
        Determines the size of the heap.

        :return int:           number of elements in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        Erases/clears out all data in the heap.
        """
        self._heap = DynamicArray()

def heapsort(da: DynamicArray) -> None:
    """
    Sorts a dynamic array as a heap, then heap sorts

    :param DynamicArray da:  a dynamic array object
    """
    if da.is_empty():
        raise MinHeapException
    # Build the heap first based off the dynamic array
    lastNonLeaf = da.length() // 2 - 1
    for nonLeaf in range(lastNonLeaf, -1, -1):
        _percolate_down(da, nonLeaf)
    
    # Start heap sorting
    k = da.length() - 1         # counter leading up to sorted nodes
    while k > 0:
        minVal = da.get_at_index(0)
        lastVal = da.get_at_index(k)
        da.set_at_index(0, lastVal)
        da.set_at_index(k, minVal)
        k -= 1
        if k > 0:
            _percolate_down(da, 0, k)

# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parentIndex: int, daWindow: int = None) -> None:
    """
    Percolates a value at the parentIndex of a heap down the tree.

    :param DynamicArray da: a dynamic array object
    :param int parentIndex: the index of the node to start percolating
    :param int daWindow:    last index of an 'unsorted heap'
    """
    # If a window is not specified, use the last index of the dynamic array
    if not daWindow:
        daWindow = da.length() - 1

    parentVal = da.get_at_index(parentIndex)
    leftIndex = parentIndex * 2 + 1
    rightIndex = parentIndex * 2 + 2

    while leftIndex <= daWindow:
        leftVal = da.get_at_index(leftIndex)
        # If theres both a left and right child of the parent
        if rightIndex <= daWindow:
            rightVal = da.get_at_index(rightIndex)
            # parentVal is less than the left and right children; done
            if parentVal < leftVal and parentVal < rightVal:
                break
            # swap parentVal with leftVal
            if leftVal <= rightVal:
                # parentVal, leftVal = leftVal, parentVal
                da.set_at_index(parentIndex, leftVal)
                da.set_at_index(leftIndex, parentVal)
                parentIndex = leftIndex    
            else:
                # swap parentVal with rightVal
                da.set_at_index(parentIndex, rightVal)
                da.set_at_index(rightIndex, parentVal)
                parentIndex = rightIndex
        # If theres only a left child of the parent
        else:
            # Parent value is properly placed
            if parentVal < leftVal:
                break
            # swap the parentVal with the leftVal
            da.set_at_index(parentIndex, leftVal)
            da.set_at_index(leftIndex, parentVal)
            parentIndex = leftIndex
        leftIndex = parentIndex * 2 + 1
        rightIndex = parentIndex * 2 + 2


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)