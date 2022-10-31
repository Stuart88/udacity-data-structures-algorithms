
Originally thought a queue structure would be best for storing
the keys as it should be possible to get the oldest cache item via
dequeueing. However, it proved problematic to handle the reordering of the
keys if/when an item is used.

After googling for more details about how an LRU cache works, I concluded
that the best option is a doubly linked list, which was most useful 
for getting the oldest item from the head of the list, and
appending youngest items to the tail.

Time efficiency:

    The problem statement demands that everything is achieved in O(1) but 
    I really cannot figure out how this is done. Most information about 
    LRU caches tell me it's O(1) at best, O(n) at worse, and this is what
    I have achieved.

Space efficiency:

    Memory required for each node in the linked list.
    During DoublyLinkedList.remove() operations, memory requirement doubles as a clone 
    list is generated.