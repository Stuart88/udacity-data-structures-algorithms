

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
            return mid_ind