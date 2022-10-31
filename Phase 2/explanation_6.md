
This felt like more of a simple algoritmic problem, since
the data structure was already decided.

Time efficiency: 

    Union: O(2n^2) -- Needs to perform sub-loop over all n in append() operation, x2

    Intersection: O(4n^2) -- Needs to perform sub-loop over all n in append() and contains() operations, x2

Space efficiency:

    Requires double the memory of original list(s) because a new list is created
    for appending the unioned / intersected items.