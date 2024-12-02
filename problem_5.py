import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp: datetime, data: str, previous_hash: str) -> None:
        self.timestamp: datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()
        self.next: Block|None = None

    def calc_hash(self) -> str:
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    def __init__(self) -> None:
        self.head: Block|None = None
        self.tail: Block|None = None

    def create_genesis_block(self) -> None:
        timestamp = datetime.now()
        genesis_block = Block(
            timestamp,
            data='genesis block',
            previous_hash='0')
        self.head = genesis_block
        self.tail = genesis_block


    def add_block(self, data: str) -> None:

        if not self.head:
            self.create_genesis_block()
        else:

            new_block = Block(timestamp=datetime.now(),data=data,previous_hash=self.tail.hash)
            self.tail.next = new_block
            self.tail = new_block

    def __repr__(self) -> str:
        curr = self.head
        blocks = []
        while curr:
            blocks.append(str(curr))
            curr = curr.next
        return "\n\n".join(blocks)

if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    # Test Case 2
    print("Test Case 2: Adding blocks to an empty blockchain")
    new_blockchain = Blockchain()
    new_blockchain.add_block("First Block")
    new_blockchain.add_block("Second Block")
    print(new_blockchain)

    # Test Case 3: Blockchain with no blocks
    print("\nTest Case 3: Blockchain with no blocks")
    empty_blockchain = Blockchain()
    print(empty_blockchain)
