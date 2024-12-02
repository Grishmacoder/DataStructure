import heapq
from collections import defaultdict
from typing import Optional

# Huffman Tree Node
class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int) -> None:
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq


def calculate_frequencies(data: str) -> dict[str, int]:
    frequency = {}
    for ch in data:
        if ch in frequency:
            frequency[ch] += 1
        frequency[ch] = 0
    return frequency

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    heap = []
    for key, freq in frequency.items():
        node = HuffmanNode(key, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)

        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    root = heapq.heappop(heap)
    return root

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    if node is None:
        return
    if node.char != None:
        huffman_codes[node.char] = code
    generate_huffman_codes(node.left, code + '0', huffman_codes)
    generate_huffman_codes(node.right, code + '1', huffman_codes)


def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    if not data:
        return "", None
    frequency = calculate_frequencies(data)
    root = build_huffman_tree(frequency)
    huffman_codes = {}
    generate_huffman_codes(root, '', huffman_codes)
    encoded_data = ''.join(huffman_codes[ch] for ch in data)
    return encoded_data,root

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    if not encoded_data or not tree:
        return  ""
    decoded_data = []
    current_node = tree
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node and current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = tree
    return ''.join(decoded_data)


# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2
    print("\nTest Case 2: Empty string")    #return empty string
    sentence = ""
    encoded_data,tree  = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data,tree)
    print("Decoded:", decoded_data)

    # Test Case 3 larger input
    print("\nTest Case 3: large sentence")
    sentence = "a"*10**6 + "b"*10**6
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data
    print("pass")

