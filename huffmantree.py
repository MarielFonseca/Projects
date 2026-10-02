
from logging import root


global str, char_binary_mapping
str = "AABBBBCCCCDEFFGHHHIIIII"
char_binary_mapping = {}


class HuffmanNode:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

def generate_tree(mapping):
    
    keyset = mapping.keys() # get all the keys in the dictionary
    priorityQ = []

    # for all char in keyset, create a node corresponding to the character and its frequency.
    for char in keyset:
        node = HuffmanNode(char, mapping[char], None, None)
        priorityQ.append(node)
        priorityQ = sorted(priorityQ, key= lambda x: x.freq) # sorting the list based on frequency


        while len(priorityQ) > 1:
            first = priorityQ.pop(0)
            second = priorityQ.pop(0)
            merged_nodes = HuffmanNode("-", first.freq + second.freq, first, second) # merge the two nodes with the lowest frequency

            priorityQ.append(merged_nodes)
            priorityQ = sorted(priorityQ, key= lambda x: x.freq)
    
    return priorityQ.pop()


def encode(streng): # gets the frequencies of each character in the string. stores in a dictionary

    mapping = {}

    for char in streng:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] += 1

    root = generate_tree(mapping)
    
    set_binary_codes(root, '')
    
    print(' char | huffman code ')
    for char in mapping:
        print('%-4r | %12s' % (char, char_binary_mapping[char]))
    
    s = '' 
    for char in streng:
        s += char_binary_mapping[char]

    return s


def set_binary_codes(node, str):
    if not node is None:
        if node.left is None and node.right is None: # leaf node
            char_binary_mapping[node.char] = str

        # left
        str += '0'
        set_binary_codes(node.left, str)
        str = str[:-1]

        # right
        str += '1'
        set_binary_codes(node.right, str)
        str = str[:-1]

        


print(encode(str))