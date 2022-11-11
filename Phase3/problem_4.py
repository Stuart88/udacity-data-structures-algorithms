
"""

The problem outline did not require any space efficiency so my original implementation was only partially correct.
After this, I researched the Dutch National Flag algorithm and implemented it correctly.
Both implementations are covered below.

### My Implementation:

    - Init a new array of 1s, same size as the input_list
    - Iterative over input list
    - If value == 0, append to front of new array
    - If value == 2, append to end of new array 
    - value == 1 can be skipped because it is enough to assign just the 0s and 2s
    - Return new array

    Time Complexity: O(n)
    Space Complexity: 2n

### The Correct Implementation:

    - Dutch National Flag algorithm
    - It is difficult to implement this without feeling like I am simply copying 
    the code from the internet. However, I did not just ctrl-C ctrl-V any solution.
    I found a step by step explanation of the algorithm and implemented each step as explained.

    Time Complexity: O(n), one traversal
    Space Complexity: n

"""

def my_implementation(input_list):
    
    final_list = [1 for i in range(len(input_list))]
    
    front_index = 0
    end_index = len(input_list) - 1

    for i in input_list:
        if i == 0:
            final_list[front_index] = 0
            front_index += 1
        elif i == 2:
            final_list[end_index] = 2
            end_index -= 1

    return final_list 

def swap_array_values(arr, index1, index2):
    val1 = arr[index1]
    val2 = arr[index2]
    arr[index1] = val2
    arr[index2] = val1
    return

def dutch_flag_algorithm(input_list):
    
    low_index = 0
    mid_index = 0
    high_index = len(input_list) - 1
    
    while mid_index <= high_index:
        if input_list[mid_index] == 0:
            swap_array_values(input_list, low_index, mid_index)
            low_index += 1
            mid_index += 1
        elif input_list[mid_index] == 1:
            mid_index += 1
        elif input_list[mid_index] == 2:
            swap_array_values(input_list, mid_index, high_index)
            high_index -= 1
    
    return input_list
    

def test_function(test_case):
    sorted_array = dutch_flag_algorithm(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])