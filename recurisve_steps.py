def steps(number, stairs = None):
    """This program determines the number of ways to climb a flight of stairs using 1, 2, or 3 steps.

    Args:
        number ([int]): the number of steps
        stairs (list, optional): The list of initial steps. Defaults to None.

    Returns:
        int: number of ways to climb the "number" of stairs using 1, 2, or 3 steps at a time.
    """
    if stairs is None:
        stairs = [1, 1, 2]
    if number + 1 == len(stairs):
        print(stairs)
        return stairs[number]
    else:
        stairs.append(stairs[-1] + stairs[-2] + stairs[-3])
        # print(stairs)
        return steps(number, stairs)
    
print(steps(10))