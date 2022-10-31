
This appears to be largely similar to a linked list, the only difference being 
that the 'value' property of a node is instead an entire Block object, 
and each block contains a reference to the hash value of the block 
that came before it.

Time efficiency (for find_block() method): 

    O(n), where n is the total number of blocks in the chain
    I considered using a map to make it faster to get a block via its hash value,
    but it seemed to still be O(n) because it would still be necessary to 
    check all keys to ensure the desired item exists. 

Space efficiency:

    Same as normal linked list.