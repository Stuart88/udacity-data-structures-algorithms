"""
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

Here is some boiler plate code and some example test cases to get you started on this problem:
"""


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.indexer = 0
        self.oldest_key = None
        pass

    def get(self, key):
        if key == None or key not in self.items:
            return -1
        val = self.items[key]
        if val is None:
            return -1
        else:
            return val

    def set(self, key, value):
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)       # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached its capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

def test_case(test_name, val, expected):
    if val == expected:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

print(our_cache.size())
print(our_cache.queue_size())
print(our_cache)

test_case('Test 0',  our_cache.get(3), -1)

# Test get None
test_case('Test 1',  our_cache.get(None), -1)

# Test get large value
test_case('Test 2', our_cache.get(9999999999999999), -1)

# Test normal get
our_cache.set(12, 87)
test_case('Test 3', our_cache.get(12), 87)

# Test use of existing key
our_cache.set(12, 99)
test_case('Test 4', our_cache.get(12), 99)

# Test string key
our_cache.set('err', 1)
test_case('Test 5', our_cache.get('err'), 1)

# Test get value for key that is too old
our_cache.set(10, 2)
our_cache.set(11, 3)
our_cache.set(12, 4)
our_cache.set(13, 5)
our_cache.set(14, 6)
our_cache.set(15, 7)
our_cache.set(16, 9)
test_case('Test 6', our_cache.get(10), -1)
