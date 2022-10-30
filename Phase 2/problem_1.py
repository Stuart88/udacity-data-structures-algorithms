
"""
For this problem we use a doubly linked list for maintaining a 'queue' of keys,
such that the oldest key is always at the head of the list. 

Cache items are stored in a dictionary, and are accessed by any given key.
Complexity: O(1)

If the key does not exist, it is prepended to the tail of the linked list, such that
it is the 'youngest' key in the cache
Complexity: Worst case O(n) to check key exists, best case O(1)

If the key already exists, it will be removed from the cache and prepended back onto 
the tail of the list, thus making it 'youngest' again
Complexity: Worst case O(n) as need to cycle through entries in removal process. Best case O(1)

If the cache is full, the oldest key is removed by getting the head of linked list
Complexity: Worst case O(n) to check and then remove key. Best case O(1)

"""

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    def size(self):
        return self.num_elements

    def prepend(self, value):
        
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is None:
            new_node.previous = self.head
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

        self.num_elements += 1
    
    def pop_head(self):
        if self.head is None:
            return None
        else:
            val = self.head.value
            new_head = self.head.next
            self.head = new_head
            self.num_elements -= 1
            return val

    def remove(self, value):
        
        if self.size() == 0:
            pass

        new_self = DoublyLinkedList()

        loop_Node = self.head

        while loop_Node is not None:
            if loop_Node.value != value:
                new_self.prepend(loop_Node.value)
            loop_Node = loop_Node.next
        
        self.head = new_self.head
        self.tail = new_self.tail
        self.num_elements -= 1

    def contains(self, value):
        if self.num_elements == 0:
            return False

        check_Node = self.head
        
        while check_Node is not None:
            if check_Node.value == value:
                return True
            check_Node = check_Node.next

        return False

    def __str__(self) -> str:
        str = ''
        head_val = self.head
        while head_val is not None:
            str += f'{head_val.value}, '
            head_val = head_val.next
        return str



class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_keys = DoublyLinkedList()
        self.cache = {}

    def get(self, key):
        if key == None or not self.cache_keys.contains(key):
            return -1
        else:
            # Get value
            val = self.cache[key]
            # Then move key to tail, i.e. make it the 'youngest key'
            self.cache_keys.remove(key)     
            self.cache_keys.prepend(key)   
            return val

    def set(self, key, value):
        if self.cache_keys.contains(key):
            # Cache already has value with key
            # Replace cache item, then move key to tail (set as 'youngest')
            self.cache[key] = value
            self.cache_keys.remove(key)
            self.cache_keys.prepend(key)
        else:
            # New key item.
            # First check if cache is full
            if self.cache_keys.size() == self.capacity:
                # Cache is full. Remove oldest key and corresponding cache value
                oldest_key = self.cache_keys.pop_head()
                del self.cache[oldest_key]
                self.cache[key] = value
                self.cache_keys.prepend(key)
            else:
                #Cache not full so just add new key
                self.cache[key] = value
                self.cache_keys.prepend(key)

    def __str__(self) -> str:
        return f'LRU Cache Details:\nCache Dictionary {self.cache}\nCache Keys: {self.cache_keys}'


def test_case(test_name, val, expected, cache: LRU_Cache):
    if len(cache.cache) > cache.capacity:
        print(f'Cache too large: ({len(cache.cache)})')
        pass
    if cache.cache_keys.size() > cache.capacity:
        print(f'Keys Cache too large: ({cache.cache_keys.size()})')
        pass
    if val == expected:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1 and sets 1 as youngest key
our_cache.get(2)       # returns 2 and sets 2 as youngest key
our_cache.get(9)       

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('\nBEGIN TESTS')

our_cache.get(3)      # Should return -1 because cache reached capacity; the '3' key was removed already
test_case('Test 0',  our_cache.get(3), -1, our_cache)

# Test get None
test_case('Test 1',  our_cache.get(None), -1, our_cache)

# Test get large value
test_case('Test 2', our_cache.get(9999999999999999), -1, our_cache)

# Test normal get
our_cache.set(12, 87)
test_case('Test 3', our_cache.get(12), 87, our_cache)

# Test re-use of existing key
our_cache.set(12, 99)
test_case('Test 4', our_cache.get(12), 99, our_cache)

# Test string key
our_cache.set('err', 1)
test_case('Test 5', our_cache.get('err'), 1, our_cache)


# Test get value for key that is too old

our_cache.set(10, 2) # <-- This should be too old, so expect -1 result
our_cache.set('a', 3)
our_cache.set('cow', 5)
our_cache.set(2, 6)
our_cache.set(1, 7)
our_cache.set('ape', 9)
test_case('Test 6', our_cache.get(10), -1, our_cache)

print('END TESTS\n')
print('Testing Complete\n')
print(our_cache)
