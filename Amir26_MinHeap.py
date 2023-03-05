# Enter your code here. Read input from STDIN. Print output to STDOUT
class MinHeap:
    def __init__(self, elements=[]):
        self.heap = []
        self.last_index = -1
        for i in elements:
            self.heap.append(i)
            self.last_index += 1
            self.__float_up(self.last_index)

    def insert(self, val):
        self.heap.append(val)
        self.last_index += 1
        # print("self heap", self.heap)
        self.__float_up(self.last_index)

    def __float_up(self, index):
        parent = (index - 1) // 2
        # print("parent, index, last index", parent, index, self.last_index)
        if parent >= 0:
            if self.heap[parent] > self.heap[index]:
                self.__swap(parent, index)
                self.__float_up(parent)
        else:
            return

    def delete(self, val):
        index = self.heap.index(val)
        self.__swap(index, self.last_index)
        self.heap.pop()
        self.last_index -= 1
        self.bubble_down(index)

    def bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left <= self.last_index:
            if self.heap[smallest] > self.heap[left]:
                self.__swap(smallest, left)
                smallest = left
                self.bubble_down(smallest)

        if right <= self.last_index:
            if self.heap[smallest] > self.heap[right]:
                self.__swap(smallest, right)
                smallest = right
                self.bubble_down(smallest)

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heap_command(self, arr):
        # print(arr)
        if arr[0] == 3:  # peek
            if self.last_index >= 0:
                _min = self.heap[0]
                print(_min)
                return _min
            else:
                return False
        elif arr[0] == 1:  # insert
            self.insert(arr[1])
        elif arr[0] == 2:  # pop
            self.delete(arr[1])


n = int(input())
Heap_test = MinHeap()
for _ in range(n):
    arr = list(map(int, input().strip().split()))
    Heap_test.heap_command(arr)