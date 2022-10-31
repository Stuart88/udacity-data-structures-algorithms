import unittest

"""
Runtime analysis:
Union complexity: O(2n^2)
Intersection complexity O(4n^2)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def contains_value(self, val):
        node = self.head
        while node:
            if node.value == val:
                return True
            node = node.next
        return False

def union(llist_1: LinkedList, llist_2: LinkedList):
    """
    Generates the union of the two given lists.
    Complexity: O(2n^2) due to list.append() method having sub-loop over all n
    """

    if llist_1 is None:
        llist_1 = LinkedList()

    if llist_2 is None:
        llist_2 = LinkedList()

    if isinstance(llist_1, LinkedList) == False:
        raise Exception('Data is not LinkedList type!')

    if isinstance(llist_2, LinkedList) == False:
        raise Exception('Data is not LinkedList type!')

    result_list = LinkedList()
    node = llist_1.head
    while node:
        result_list.append(node.value)
        node = node.next
    
    node = llist_2.head
    while node:
        result_list.append(node.value)
        node = node.next
    
    return result_list

def intersection(llist_1, llist_2):
    """
    Generates the intersection of the two given lists.
    Complexity: O(4n^2)
    """
    if llist_1 is None:
        llist_1 = LinkedList()

    if llist_2 is None:
        llist_2 = LinkedList()

    if isinstance(llist_1, LinkedList) == False:
        raise Exception('Data is not LinkedList type!')

    if isinstance(llist_2, LinkedList) == False:
        raise Exception('Data is not LinkedList type!')

    result_list = LinkedList()
    node = llist_1.head
    while node:
        if result_list.contains_value(node.value) == False:
            result_list.append(node.value)
        node = node.next
    
    node = llist_2.head
    while node:
        if result_list.contains_value(node.value) == False:
            result_list.append(node.value)
        node = node.next
    
    return result_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


def test_case(test_name: str, result, expected):
    if result == expected:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')


# Test one empty input
result = union(linked_list_1, None)
test_case('Test 1', result.size(), linked_list_1.size())

# Test both empty inputs
result = intersection(None, None)
test_case('Test 2', result.size(), 0)

# Test raise exception on incorrect data type

class ExceptionTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            intersection([1,4,5], None)

        if context.exception.args[0] == 'Data is not LinkedList type!':
            print('Exception test Passed')
        else:
            print('Exception test Failed')


test_exception = ExceptionTestCase()
test_exception.test()