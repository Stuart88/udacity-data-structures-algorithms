

"""
Rearranges array elements so as to form two numbers such that their sum is maximum.

First performs merge sort into descending order.

Then iteratively appends each value to two strings in an alternating pattern.
This works because we want the highest two values to be assigned as (for example) hundreds,
then the next highest to be assigned as tens, etc etc.

E.g: [9,8,7,6,5,4]

First, 900+800 yields highest 'hundreds' value
Then, 70+60 yields highest 'tens' value
Then, 5+4 remains
Solution, [975, 864]

Hence the prescribed logic works.

Time Complexity: O(nlogn) like standard merge sort
Space Complexity: Requires additional memory for creating new arrays during sort 

"""

def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def rearrange_digits(input_list):

    sorted_list = mergesort(input_list)

    left = ''
    right = ''
    for i in range(len(sorted_list)):
        if i % 2 == 0 :
            left += str(sorted_list[i])
        else:
            right += str(sorted_list[i])

    return int(left), int(right)
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[9, 7, 6, 8, 5, 4], [975, 864]])
