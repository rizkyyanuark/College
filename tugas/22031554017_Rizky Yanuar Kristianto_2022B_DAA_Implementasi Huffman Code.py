import heapq
from collections import defaultdict, Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq_counter = Counter(text)
    min_heap = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right

        heapq.heappush(min_heap, merged_node)

    return min_heap[0]


def build_huffman_codes(root, current_code='', huffman_codes={}):
    if root is not None:
        if root.char is not None:
            huffman_codes[root.char] = current_code
        build_huffman_codes(root.left, current_code + '0', huffman_codes)
        build_huffman_codes(root.right, current_code + '1', huffman_codes)


def huffman_encoding(text):
    if not text:
        return None, {}

    root = build_huffman_tree(text)
    huffman_codes = {}
    build_huffman_codes(root, '', huffman_codes)

    encoded_text = ''.join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes


def huffman_decoding(encoded_text, huffman_codes):
    if not encoded_text:
        return None

    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        for char, code in huffman_codes.items():
            if code == current_code:
                decoded_text += char
                current_code = ''
                break

    return decoded_text


text = 'Rizky Yanuar Kristianto'
encoded_text, huffman_codes = huffman_encoding(text)
print('Encoded Text:', encoded_text)
decoded_text = huffman_decoding(encoded_text, huffman_codes)
