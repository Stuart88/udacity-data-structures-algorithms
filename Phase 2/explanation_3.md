
Uses a priority queue for generating Huffman tree from the raw character frequency data.
Tree node generation methods use recursion (see convert_nodes_to_huffman_tree() method)

Time efficiency: 

    O(nlogn)

    Reason: All processes are O(n), apart from the get_character_data_codes() method
    which is O(nlogn), hence this represents the worst case scenario (for large n 
    in a message where all characters are unique)

Space efficiency:

    Uses a single HuffmanTree object which contains:
    - EncodingsList
        The EncodingsList contains a collection of objects holding the necessary data for
        generating the Huffman Tree (character, frequency, huffman code)

    - HuffmanPriorityQueue
        The HuffmanPriorityQueue contains a list of HuffmanTreeNode objects that
        are used to generate the final HuffmanTree

        HuffmanPriorityQueue is deleted after the full Huffman tree has been generated

    - HuffmanTreeNode
        Contains properties necessary for processing and handling each node during
        traversal of the Huffman tree

    

    