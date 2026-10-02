
from logging import root
from typing import Counter


class HuffmanNode:
    def __init__(self, token, freq, left = None, right = None):
        self.token = token
        self.freq = freq
        self.left = left
        self.right = right

def generate_tree(frequencies):
    
    priorityQ = [
        HuffmanNode(token, freq)
        for token, freq in frequencies.items()
    ]

    priorityQ.sort(key=lambda node: node.freq)

    while len(priorityQ) > 1:
        first = priorityQ.pop(0)
        second = priorityQ.pop(0)
        merged_nodes = HuffmanNode(
            None, first.freq + second.freq, first, second
        ) # merge the two nodes with the lowest frequency
        priorityQ.append(merged_nodes)
        priorityQ.sort(key= lambda node: node.freq)
    
    return priorityQ[0]

def set_binary_codes(node, prefix, codes):
    if not node.token is None: # leaf node
        codes[node.token] = prefix or "0"
        return

    set_binary_codes(node.left, prefix + "0", codes)
    set_binary_codes(node.right, prefix + "1", codes)

def encode(streng): # gets the frequencies of each character in the string. stores in a dictionary

    words = streng.split()
    if not words:
        return '', {}

    frequencies = Counter(words)
    root = generate_tree(frequencies)

    codes = {}
    set_binary_codes(root, '', codes)
    encoded = "".join(codes[word] for word in words)
    return encoded, codes


text = "samurais fight ninjas"
encoded, codes = encode(text)

print("Word | Huffman code")
for word, code in codes.items():
    print(f"{word!r} | {code}")

print("Encoded: ", encoded)