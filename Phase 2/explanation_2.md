
Uses recursion to check sub directories.

Reasoning: Cleaner than iterating through all items using sub-loops.

Time efficiency: 

    O(n), where n is total number of directory paths and file paths

Space efficiency:

    As far as I can see, this requires only the amount of space that is
    necessary for reading the directory using the in-built 'os' library,
    and the space rquired for adding each path to the final array.