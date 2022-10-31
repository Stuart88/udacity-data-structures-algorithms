import sys

"""
Implementation of Huffman encoding for lossless data compression.
Uses binary tree structure and an 'EncodingData' class which holds information 
about the frequency and encoding value for each character in the given message.

Complexity: O(nlogn)

Reason: All processes are O(n), apart from the get_character_data_codes() method
which is O(nlogn), hence this represents the worst case scenario for large n 
in a message where all characters are unique
"""

class HuffmanTreeNode:
    def __init__(self, char: str, freq: int) -> None:
        self.left: HuffmanTreeNode = None
        self.right: HuffmanTreeNode = None
        self.parent: HuffmanTreeNode = None
        self.char: str = char
        self.frequency: int = freq
        self.bit_value: str = ''
        self.huffman_code: str = ''
        self.scanned: bool = False
    
    def is_leaf_node(self):
        return self.left is None and self.right is None 
    
    def __repr__(self) -> str:
        return f'{self.char}:{self.frequency}'

class EncodingData:
    def __init__(self, char: str, freq: int, code: str) -> None:
        self.char = char
        self.freq = freq
        self.code = code
    
    def __repr__(self) -> str:
        return f'{self.char}:{self.freq}:{self.code}'

class EncodingsList:
    def __init__(self) -> None:
        self.items: list[EncodingData] = []
    
    def append(self, item: EncodingData):
        self.items.append(item)
    
    def contains_char(self, char: str):
        if char is None:
            return False
        for i in range(len(self.items)):
            if self.items[i].char == char:
                return True
        return False
    
    def size(self):
        return len(self.items)

    def add_code(self, key, code):
        for i in self.items:
            if i.char == key:
                i.code = code
                return
        pass
    
    def encoded_items_count(self):
        count = 0
        for i in self.items:
            if i.code != '' and i.code != None:
                count += 1
        return count

    def get_code_for_character(self, char):
        for i in self.items:
            if i.char == char:
                return i.code
        return ''

class HuffmanPriorityQueue:
    def __init__(self) -> None:
        self.items: list[HuffmanTreeNode] = []
        self.num_elements = 0

    def append(self, node: HuffmanTreeNode):
        self.items.append(node)
        self.num_elements += 1

    def sort(self) -> None:
        """Sorts items by frequency of characters, highest to lowest"""
        self.items.sort(key=lambda x: x.frequency, reverse=True)

    def size(self):
        return self.num_elements

    def pop_smallest_two(self):
        
        if self.size() < 2:
            raise Exception('Priority Queue does not have enough data to pop two values!') 
        
        self.num_elements -= 2
        node_left = self.items.pop()
        node_right = self.items.pop()
        return node_left, node_right

class HuffmanTree:
    def __init__(self, message: str) -> None:
        self.message: str = message
        self.character_data: EncodingsList = self.determine_character_frequencies(self.message)
        self.nodes_list: HuffmanPriorityQueue = self.generate_tree_nodes(self.character_data)
        self.root: HuffmanTreeNode = self.convert_nodes_to_huffman_tree(self.nodes_list)

    def determine_character_frequencies(self, message: str) -> EncodingsList:
        """
        Finds the frequency of each character occurrence in the given message,
        and stores results in EncodingsList object for future use
        Complexity: O(n) 
        Worst case O(2n) if frequencies_dict is all unique values
        """
        frequencies_dict = {}
        
        for c in message:
            if c in frequencies_dict:
                val = frequencies_dict[c]
                val += 1
                frequencies_dict[c] = val
            else:
                frequencies_dict[c] = 1

        encodings_data = EncodingsList()

        for v in frequencies_dict:
            encodings_data.append(EncodingData(v, frequencies_dict[v], ''))


        return encodings_data
    
    
    def generate_tree_nodes(self, encoding_items: EncodingsList) -> HuffmanPriorityQueue:
        """ 
        Converts a dictionary of { key = char, val = freq }
        into a list of HuffmanTreeNode objects.
        Complexity: O(n)
        """
        node_list = HuffmanPriorityQueue()

        for i in encoding_items.items:
            new_node = HuffmanTreeNode(i.char, i.freq)
            node_list.append(new_node)

        node_list.sort()

        return node_list

    def convert_nodes_to_huffman_tree(self, nodes: HuffmanPriorityQueue) -> HuffmanTreeNode:
        """
        Converts Huffman priority queue of character freqyency data into binary tree root
        via recursive generation.
        """
        processed_queue = self.generate_huffman_nodes(nodes)        
        return processed_queue.items[0]
        

    def generate_huffman_nodes(self, nodes: HuffmanPriorityQueue) -> HuffmanPriorityQueue:
        """
        Recursively processes priority queue items into Huffman Tree, i.e.
        a PriorityQueue with a single remaining Huffman Tree node entry that contains all other nodes
        as children in a binary tree arrangement.
        Complexity: O(n)

        """
        if nodes.size() == 1:
            return nodes

        node_left, node_right = nodes.pop_smallest_two()
        
        node_left.bit_value = '0'
        node_right.bit_value = '1'

        new_node = HuffmanTreeNode(None, node_left.frequency + node_right.frequency)
        node_left.parent = new_node
        node_right.parent = new_node

        new_node.left = node_left
        new_node.right = node_right
        
        
        nodes.append(new_node)
        nodes.sort()
        
        return self.generate_huffman_nodes(nodes)

    def get_character_data_codes(self):
        """
        Traverses Huffman tree to find binary code value
        of each character in character_data.
        Complexity: O(nlogn)
        Reason: The traversal runs the whole tree n times, but on
        each traversal only goes as far as the latest unscanned node. Each scan 
        decrements the distance needing to be traversed, hence it is O(nlogn), as opposed
        to n^2 if the whole tree is traversed on each run
        """

        current_node:HuffmanTreeNode = self.root
        node_code:str = ''

        while self.character_data.encoded_items_count() != self.character_data.size():

            if current_node.left is not None and current_node.left.scanned == False:
                # Traverse left
                current_node = current_node.left
                node_code += current_node.bit_value

            elif current_node.right is not None and current_node.right.scanned == False:
                # Traverse right
                current_node = current_node.right
                node_code += current_node.bit_value

            else:
                # Left and right already traversed.
                # Mark current_node as scanned and move back to parent
                current_node.scanned = True
                current_node = current_node.parent
                node_code = node_code[0:-1] # Remove the bit value that was added on

            if current_node.char is not None:
                self.character_data.add_code(current_node.char, node_code)
                current_node.scanned = True
                current_node = self.root
                node_code = ''
        
    
    def generate_huffman_code(self) -> str:
        """
        Creates final encoding of the given data.
        Traverses Huffman tree nodes and appends binary code value to string result.
        Complexity: O(n)
        """
        
        self.get_character_data_codes()
        

        final_code = ''

        for c in self.message:
            final_code += self.character_data.get_code_for_character(c)
        
        return final_code

    def decode_data(self, data: str):
        """
        Iterates over the given encoded data and converts each item
        into relevant character values from the leaves of the Huffman Tree
        Complexity: O(n)
        """
        decoded_data = ''
        current_node = self.root
        for i in data:
            if i == '0':
                current_node = current_node.left
                if current_node.is_leaf_node():
                    decoded_data += current_node.char
                    current_node = self.root
            if i == '1':
                current_node = current_node.right
                if current_node.is_leaf_node():
                    decoded_data += current_node.char
                    current_node = self.root
        
        return decoded_data
            

def huffman_encoding(data):
    tree = HuffmanTree(data)
    return tree.generate_huffman_code(), tree

def huffman_decoding(data, tree: HuffmanTree):
    return tree.decode_data(data)
    

def handle_data(data, print_data_sizes: bool):

    if data is None:
        return None

    if isinstance(data, str) == False:
        return None

    if len(data) == 0:
        return None

    if print_data_sizes:
        print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
        #print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    if print_data_sizes:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        #print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    if print_data_sizes:
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        #print ("The content of the decoded data is: {}\n".format(decoded_data))

    return decoded_data

def test_case(test_name, message, expected_result, print_data_sizes):
    res = handle_data(message, print_data_sizes)
    if res == expected_result:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

super_long_str = """This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long string This is a super long string This is a3432 super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long str32432ing This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long string This is 43a543 sfdper long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long strinwerewg This is a super longfdgg435543 string This ewr string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long string This is a super long4ong string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long strisdfdng This is a super 45ring This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string Terhis is a super long string This is a sugdsfper long string Thfgis is a23432 supeglong string This is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super longdfetrestring This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This iwsre a super long string This is a supe3243r long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long strThis is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is a super long3432 string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This is werewa super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringing This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string
This is a super long string This 432is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long stringThis is a super long string This is a super long string This is a super long string This is a super long string"""

normal_string = "The bird is the word"

print_data_sizes = True

test_case('Test 1', super_long_str, super_long_str, print_data_sizes)
test_case('Test 2', None, None, print_data_sizes)
test_case('Test 3', 12345, None, print_data_sizes)
test_case('Test 4', normal_string, normal_string, print_data_sizes)
