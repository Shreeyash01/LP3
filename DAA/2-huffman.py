import heapq

class MinHeapNode:
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None

def print_codes(root, s):
    if root is None:
        return

    if root.data != '$':
        print(root.data, ":", s)

    print_codes(root.left, s + "0")
    print_codes(root.right, s + "1")

def huffman_codes(data, freq):
    heap = []
    for i in range(len(data)):
        node = MinHeapNode(data[i], freq[i])
        heapq.heappush(heap, (freq[i], i, node))

    # print("Min Heap:")
    # for i in heap:
    #     print(i)
    # print("\n")

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)
        top = MinHeapNode('$', freq1 + freq2)
        top.left = left
        top.right = right
        heapq.heappush(heap, (freq1 + freq2, i, top))

    print("Huffman Codes:")
    print_codes(heap[0][2], "")

arr = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [50, 10, 30, 5, 3, 2]

huffman_codes(arr, freq)