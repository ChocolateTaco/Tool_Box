# Name:             Steven Tran
# OSU Email:        trans4@oregonstate.edu
# Course:           CS261 - Data Structures
# Assignment:       Assignment 5
# Due Date:         2022-05-23
# Description:      An overview of the Dynamic Array ADT, which is a static
#                   array that can increase/decrease its memory allocation or 
#                   capacity. Updated to include pop and support heap 
#                   functionality.

from static_array import StaticArray

class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
                raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Either shrinks the dynamic array object or enlarges it

        :param int new_capacity: Size of the dynamic array to be
        """
        
        if new_capacity <= 0 or new_capacity < self.length():
            return
        self._capacity = new_capacity
        newArray = StaticArray(new_capacity)

        if not self.is_empty():
            for element in range(0, self.length()):
                newArray.set(element, self.get_at_index(element))
        self._data = newArray

    def append(self, value: object) -> None:
        """
        Adds elements to the dynamic array

        :param object value: A numeric element
        """
        if self.length() + 1 <= self.get_capacity():
            self._data[self._size] = value
            self._size += 1
        elif self.length() + 1 > self.get_capacity():
            self.resize(self.get_capacity() * 2)
            self._data[self._size] = value
            self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a value at a valid index location.

        :param int index: index location
        :param object value: numerical value to be placed

        :raises DynamicArrayException: invalid index access
        """
        inserted = False
        
        # Check if index is invalid
        if index < 0 or index >= self.length() + 1:
            raise DynamicArrayException

        # Determine if resize is required
        if self.length() + 1 > self.get_capacity():
            self.resize(self.get_capacity() * 2)
        
        for element in range(self.length() + 1):
            if inserted == False:
                # Begin insertion
                if index == element:
                    saveOne = self._data[element]   # save removed index
                    self._data[element] = value
                    self._size += 1
                    inserted = True
            else:   # inserted == True
                # save 2nd removed index before insertion
                saveTwo = self._data[element]           
                self._data[element] = saveOne
                saveOne = saveTwo

    def remove_at_index(self, index: int) -> None:
        """
        Removes an element at a specified index. The dynamic array will be 
        reduced in size if the length is 1/4 of its current capacity. Max 
        reduced size is 10.

        :param int index:               index of element to be removed

        :raises DynamicArrayException:  invalid index access
        """
        # size = self.length()
        # capacity = self.get_capacity()

        if index < 0 or index >= self.length():
            raise DynamicArrayException

        # Determine if resizing is required
        if (self.length()/self.get_capacity() < .25) and (self.get_capacity() > 10):
            if self.length() * 2 < 10:
                self.resize(10)
            else:
                self.resize(self.length() * 2)
        # Start Removal Process
        removed = False
        for element in range(0, self.length()):
            if removed is False:
                if index == element:
                    self._size -= 1
                    self._data[element] = None
                    removed = True
            else:
                temp = self._data[element - 1]
                self._data[element - 1] = self._data[element]
                self._data[element] = temp

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Cuts a slice of the dynamic array from a starting index of a certain
        specified length (size).

        :param int start_index:     first index of the slice
        :param int size: number     of elements in the slice

        :raises DynamicArrayException: invalid index access

        :return DynamicArray:       a Dynamic Array object
        """
        if start_index < 0 or start_index >= self.length() or size < 0:
            raise DynamicArrayException
        if start_index + size - 1 < self.length():
            sliced = DynamicArray()
            for element in range(start_index, start_index + size):
                sliced.append(self._data[element])
        else:
            raise DynamicArrayException
        return sliced

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Combines a second dynamic array with the existing array (self)

        :param DynamicArray second_da: second dynamic array object
        """
        for element in range(second_da.length()):
            self.append(second_da.get_at_index(element))


    def map(self, map_func) -> "DynamicArray":
        """
        Generates a dynamic array full of elements mapped by a function.

        :param function map_func:   some function

        :return DynamicArray:       a Dynamic Array object
        """
        someDynamicArray = DynamicArray()
        for item in range(self.length()):
            someDynamicArray.append(map_func(self._data[item]))
        
        return someDynamicArray

    def filter(self, filter_func) -> "DynamicArray":
        """
        Creates a dynamic array object for only the filtered items

        :param function filter_func: some function containing a search filter

        :return DynamicArray:        a Dynamic Array object
        """
        someDynamicArray = DynamicArray()
        for item in range(self.length()):
            if filter_func(self._data[item]):
                someDynamicArray.append(self._data[item])
        
        return someDynamicArray

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        _summary_

        :param _type_ reduce_func:  an iterable function
        :param _type_ initializer:  first iteration for the function, defaults 
                                    to None

        :return object:             a single result from the reduce_funct 
                                    iterated throughout the array
        """
        someDynamicArray = DynamicArray()
        result = None
        if initializer:
            result = initializer
            for item in range(self.length()):
                result = reduce_func(result, self._data[item])
        else:
            result = self._data[0]
            for item in range(1, self.length()):
                result = reduce_func(result, self._data[item])
        return result

    def pop(self) -> object:
        """
        Returns the last populated element of the dynamic array, and removes it.

        :return object:     some data element
        """
        last_populated_idx = self.length() - 1
        if last_populated_idx >= 0:
            popped = self.get_at_index(last_populated_idx)
            self.set_at_index(last_populated_idx, None)
            self._size -= 1
        else:
            raise DynamicArrayException
        return popped


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Finds the mode of a dynamic array object; the most frequent element.

    :param DynamicArray arr:    a Dynamic Array object

    :return tuple:              a tuple containing:
                                1) element(s) of the mode
                                2) the mode/# of instances
    """
    highScoreValue = None
    highScoreInstances = 0
    # Pointer for the challenging mode contender
    contenderValue = None
    contenderInstances = 0

    index = 0
    arrayLength = arr.length()
    modeArray = DynamicArray()

    while index < arrayLength:
        # 1st index = the "high score"
        if highScoreValue is None:              
            highScoreValue = arr.get_at_index(index)
            highScoreInstances += 1
            modeArray.append(highScoreValue)
        # Increases the high score's instances if the array element matches
        elif arr.get_at_index(index) == highScoreValue:  
            highScoreInstances += 1
        # Increase the contender's instances & check if it beats the current 
        # high score
        elif arr.get_at_index(index) == contenderValue:  
            contenderInstances += 1
            # If contender is the new Mode
            if contenderInstances > highScoreInstances:
                modeArray = DynamicArray()
                modeArray.append(contenderValue)
                highScoreValue = contenderValue
                highScoreInstances = contenderInstances
            # If theres a tie for the array's mode(s)
            elif contenderInstances == highScoreInstances:
                modeArray.append(contenderValue)
        else:    
            # New Value is encountered that is neither the existing high score 
            # nor contender's value
            contenderValue = arr.get_at_index(index)
            contenderInstances = 1
            if contenderInstances == highScoreInstances:
                modeArray.append(contenderValue)
        index += 1
    
    return (modeArray, highScoreInstances)


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
