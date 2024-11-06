import heapq
from collections import defaultdict, Counter


# Class to represent a node in the Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define the comparison operator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to calculate the frequency of each character in the input data
def calculate_frequency(data):
    return Counter(data)


# Function to build the Huffman Tree using a priority queue (min-heap)
def build_huffman_tree(freq):
    priority_queue = []

    # Create a leaf node for each character and add it to the priority queue
    for key, value in freq.items():
        node = HuffmanNode(key, value)
        heapq.heappush(priority_queue, node)

    # Iterate until only one node remains in the priority queue
    while len(priority_queue) > 1:
        # Extract the two nodes with the lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with a frequency equal to the sum of the two nodes
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Add the new node back to the priority queue
        heapq.heappush(priority_queue, merged)

    # The remaining node is the root of the Huffman tree
    return heapq.heappop(priority_queue)


# Function to generate the Huffman codes for each character by traversing the tree
def generate_huffman_codes(node, current_code="", codes={}):
    if node is None:
        return

    # If it's a leaf node, assign the current code
    if node.char is not None:
        codes[node.char] = current_code

    # Traverse the left and right children
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)

    return codes


# Function to encode the input data using the generated Huffman codes
def huffman_encode(data, codes):
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    return encoded_data


# Function to perform Huffman Encoding
def huffman_encoding(data):
    # Step 1: Calculate frequency of each character
    frequency = calculate_frequency(data)

    # Step 2: Build Huffman Tree
    huffman_tree = build_huffman_tree(frequency)

    # Step 3: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree)

    # Step 4: Encode the data
    encoded_data = huffman_encode(data, huffman_codes)

    return encoded_data, huffman_codes


# Function to decode the encoded data
def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = ""
    current_node = huffman_tree

    # Traverse the tree using the encoded data
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # If a leaf node is reached, append the character to the result
        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.char
            current_node = huffman_tree

    return decoded_data


# Main program
if __name__ == "__main__":
    # Input data
    data = input("Enter the data to be encoded: ")

    # Perform Huffman Encoding
    encoded_data, huffman_codes = huffman_encoding(data)

    # Display the Huffman Codes and Encoded Data
    print("\nHuffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print(f"\nEncoded Data: {encoded_data}")

    # Decode the data
    huffman_tree = build_huffman_tree(calculate_frequency(data))
    decoded_data = huffman_decoding(encoded_data, huffman_tree)

    print(f"\nDecoded Data: {decoded_data}")
