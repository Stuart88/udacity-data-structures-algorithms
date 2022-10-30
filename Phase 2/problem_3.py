import sys

class HuffmanTreeNode:
    def __init__(self, char: str, freq: int) -> None:
        self.left: HuffmanTreeNode = None
        self.right: HuffmanTreeNode = None
        self.parent: HuffmanTreeNode = None
        self.char: str = char
        self.frequency: int = freq
        self.bit_value: str = ''
        self.huffman_code: str = ''

class EncodingData:
    def __init__(self, char: str, freq: int, code: str) -> None:
        self.char = char
        self.freq = freq
        self.code = code
        pass

class EncodingsList:
    def __init__(self) -> None:
        self.items = []
    
    def append(self, item):
        self.items.append(item)
    
    def contains_char(self, char: str):
        if char is None:
            return False
        for i in range(len(self.items)):
            if self.items[i].char == char:
                return True
        return False

class PriorityQueue:
    def __init__(self) -> None:
        self.items = []
        self.num_elements = 0

    def append(self, node: HuffmanTreeNode):
        self.items.append(node)
        self.num_elements += 1

    def sort(self) -> None:
        self.items.sort(key=lambda x: x.frequency)

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
        self.character_freqs: dict = self.determine_character_frequencies(self.message)
        self.nodes_list: PriorityQueue = self.generate_tree_nodes(self.character_freqs)
        self.root: HuffmanTreeNode = self.convert_nodes_to_huffman_tree(self.nodes_list)
        self.current_encodings: EncodingsList = EncodingsList()

    def determine_character_frequencies(self, message: str) -> dict:
        
        frequencies_dict = {}
        
        for c in message:
            if c in frequencies_dict:
                val = frequencies_dict[c]
                val += 1
                frequencies_dict[c] = val
            else:
                frequencies_dict[c] = 1
        
        dict(sorted(frequencies_dict.items(), key=lambda item: item[1]))

        return frequencies_dict
    
    
    def generate_tree_nodes(self, dict: dict) -> PriorityQueue:
        """ 
        Converts a dictionary of { key = char, val = freq }
        into a list of HuffmanTreeNode objects.
        
        """
        node_list = PriorityQueue()

        for i in dict:
            new_node = HuffmanTreeNode(i, dict[i])
            node_list.append(new_node)

        node_list.sort()

        return node_list

    def convert_nodes_to_huffman_tree(self, nodes: PriorityQueue) -> HuffmanTreeNode:
        processed_queue = self.recursively_generate_huffman_nodes(nodes)        
        return processed_queue.items[0]
        

    def recursively_generate_huffman_nodes(self, nodes: PriorityQueue) -> PriorityQueue:
        """
        Recursively processes priority queue items into Hoffman Tree, i.e.
        a PriorityQueue with a single remaining Hoffman Tree node entry that contains all other nodes
        as children in a Hoffman Tree arrangement.

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
        
        return self.recursively_generate_huffman_nodes(nodes)

    def get_min_node(self, node: HuffmanTreeNode, current_encodings: EncodingsList) -> HuffmanTreeNode:
        current_node = node
        while current_node.left is not None or current_node.right is not None:
            if current_node.left is not None and current_encodings.contains_char(current_node.left.char) == False:
                current_node = self.get_min_node(current_node.left, current_encodings)
            elif current_node.right is not None and current_encodings.contains_char(current_node.right.char) == False:
                current_node = self.get_min_node(current_node.right, current_encodings)

        return current_node
    
    def generate_huffman_code(self) -> str:

        current_node:HuffmanTreeNode = self.get_min_node(self.root, self.current_encodings)

        while current_node.parent is not None:
            node_code = ''
            loop_node = current_node
            while loop_node is not None:
                node_code += loop_node.bit_value
                loop_node = loop_node.parent
            self.current_encodings.append(EncodingData(current_node.char, current_node.frequency, node_code))
            current_node = current_node.parent
            

        final_code = ''

        for c in self.message:
            for i in self.current_encodings.items:
                if c == i.char:
                    final_code += c
        
        return final_code
            
        
        


    


           
        


def huffman_encoding(data):
    tree = HuffmanTree(data)
    return tree.generate_huffman_code(), tree

def huffman_decoding(data,tree: HuffmanTree):
    decoded_data = ''
    current_node = tree.root
    for i in data:
        if i == '0':
            if current_node.left is None:
                decoded_data += current_node.char
                current_node = tree.root
            else:
                current_node = current_node.left
        if i == '1':
            if current_node.right is None:
                decoded_data += current_node.char
                current_node = tree.root
            else:
                current_node = current_node.right

    return decoded_data


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    a_great_sentence = 'AAAAAAABBBCCCCCCCDDEEEEEE'

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3