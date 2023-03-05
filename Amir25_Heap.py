class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = []
        self.last_index = -1
        for i in elements:
            self.heap.append(i)
            self.last_index += 1
            self.__float_up(self.last_index)

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __float_up(self, index):
        parent = (index-1)//2
        if parent < 0:
            return
        else:
            if self.heap[parent]<self.heap[index]:
                self.__swap(parent, index)
                self.__float_up(parent)

    def insert(self, element):
        self.heap.append(element)
        self.last_index += 1
        self.__float_up(self.last_index)

    def pop_max(self):
        self.__swap(self.last_index, 0)
        _max = self.heap.pop()
        self.last_index -= 1
        self.bubble_down(0)
        return _max

    def peek(self):
        if self.heap[0]:
            return self.heap[0]
        else:
            return False

    def bubble_down(self, index):
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        largest = index
        if self.last_index >= left_child and self.heap[left_child] > self.heap[largest]:
            self.__swap(left_child, largest)
            largest = left_child
            self.bubble_down(largest)
        if self.last_index >= right_child and self.heap[right_child] > self.heap[largest]:
            self.__swap(right_child, largest)
            largest = right_child
            self.bubble_down(largest)


heap_test = MaxHeap([1, 5, 3, 9, 11, 87])
print(heap_test.heap)
heap_test.insert(55)
print(heap_test.heap)
heap_test.pop_max()
print(heap_test.heap)
print(heap_test.peek())