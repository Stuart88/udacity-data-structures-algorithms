

"""
Finding a number in a rotated array

This method first uses binary search to find the pivot index about which the rotation occurred.

The pivot index marks the point at which the first step of the binary search should divide the given input array

After this, normal binary search is used.

Complexity: O(logn), like normal binary search
Space: O(n) representing space required by input array
"""

def find_pivot(arr):
    """
    Finds the index at which array has been rotated
    For example [6, 7, 8, 9, 10, 1, 2, 3, 4] would return 4  
    """

    if arr == None or len(arr) == 0:
        return None

    start_index = 0
    end_index = len(arr) - 1

    # First check for array not rotated. Return last index if not rotated
    if arr[0] < arr[end_index]:
        return end_index
    
    mid_index = end_index // 2

    while end_index - start_index > 1:
        
        left_in_order = arr[start_index] < arr[mid_index]
        right_in_order = arr[end_index] > arr[mid_index + 1]   
        
        if left_in_order and right_in_order: # We are on the pivot now
            return mid_index

        if right_in_order: # Right side is in order so we can ignore this
            end_index = mid_index
        else:              # Left side is in order so ignore this
            start_index = mid_index

        mid_index = start_index + ((end_index - start_index) // 2)
    
    return start_index
        
        


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # Get pivot of rotated array
    pivot = find_pivot(input_list)
    
    start_index = 0
    end_index = len(input_list) - 1

    # Only need to search on side of array that has the correct range of values to search
    if input_list[0] > number and input_list[pivot] > number:
        # Number is not in left side
        start_index = pivot    
    else:
        end_index = pivot

    # Now perform standard binary search in remaining set of ordered numbers

    mid_index = start_index + ((end_index - start_index) // 2)

    while end_index - start_index > 1:
        if input_list[mid_index] == number:
            return mid_index

        if input_list[mid_index] > number:
            end_index = mid_index
        else:             
            start_index = mid_index

        mid_index = start_index + ((end_index - start_index) // 2)
    
    # Loop broke out because start and end met
    # Final check of those indices
    if input_list[start_index] == number:
        return start_index
    if input_list[end_index] == number:
        return end_index

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_find_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if find_pivot(input_list) == number:
        print("Pass")
    else:
        print("Fail")

print('Test finding pivot')
test_find_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])
test_find_function([[5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 5])
test_find_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_find_function([[6, 7, 8, 9, 2, 3, 4], 3])
test_find_function([[6, 7, 8, 9, 10, 11, 12], 6])
print('')

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print('Test search rotated arrays')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])