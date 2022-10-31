from datetime import date, datetime
import hashlib

class Block:

    def __init__(self, timestamp: datetime, data: str, previous_hash: str) -> None:
      self.timestamp: datetime = timestamp
      self.data:str = data
      self.previous_hash:str = previous_hash
      self.hash:str = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockNode:

    def __init__(self) -> None:
        self.block_data: Block = None
        self.prev: BlockNode = None
        self.next: BlockNode = None

class Blockchain:

    def __init__(self) -> None:
        self.head: BlockNode = None
        self.num_elements = 0

    def append_data(self, data: str):
        if isinstance(data, str) == False:
            return

        new_block_node = BlockNode()
        if self.head is None:
            new_block_node.block_data = Block(date.today(), data, None) 
            self.head = new_block_node
        else:
            new_block_node.block_data = Block(date.today(), data, self.head.block_data.hash) 
            self.head.prev = new_block_node
            new_block_node.next = self.head
            self.head = new_block_node
        
        self.num_elements += 1
    
    def size(self):
        return self.num_elements

    def find_block(self, hash:str) -> Block:
        
        if isinstance(hash, str) == False:
            return None

        check_node = self.head

        while check_node is not None:
            if check_node.block_data.hash == hash:
                return check_node.block_data
            check_node = check_node.next
        
        return None

def test_case(test_name: str, result, expected):
    if result == expected:
        print(f'{test_name} Passed')
    else:
        print(f'{test_name} Failed')

def calc_hash(data: str) -> str:
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

blockchain = Blockchain()

blockchain.append_data("Here's my data")
blockchain.append_data("Here's some other data")
blockchain.append_data("This is more data")

# Test blockchain is expected size
test_case('Test 1', blockchain.size(), 3)

# Test retrieve data by hash value
calculated_hash = calc_hash("This is more data")
found_block = blockchain.find_block(calculated_hash)
test_case('Test 2', found_block.hash, calculated_hash)

# Test chain is working, by checking the retrived block is holding the correct previous_hash data
calculated_previous_hash = calc_hash("Here's some other data")
test_case('Test 3', found_block.previous_hash, calculated_previous_hash)

# Test null data
test_case('Test 4', blockchain.find_block(None), None)

# Test large, non-string data provided to block
blockchain.append_data(99999999999999999999999999)
test_case('Test 5', blockchain.size(), 3) # Size should still be 3 because the appended data was rejected
test_case('Test 6', blockchain.find_block(99999999999999999999999999), None)



