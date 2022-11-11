

"""
Finds min and max by single traversal.
Compares each value against stored min and max,
and updates min or max if necessary.

Time Complexity: O(n)
Space Complexity: n

"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = 0
    min = 0

    for i in ints:
        if i > max:
            max = i
        elif i < min:
            min = i
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")