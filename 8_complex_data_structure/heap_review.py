### IMPORT --------------------------------
from random import randrange

### CLASS DECLARATION ----------------------
class MinHeap:
    
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print("Adding {} to {}.".format(element, self.heap_list))
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()

    def parent_idx(self, idx):
        # Helper Method
        return idx // 2

    def left_child_idx(self, idx):
        # Helper Method
        return idx * 2

    def right_child_idx(self, idx):
        # Helper Method
        return idx * 2 + 1

    def heapify_up(self):
        print("Restoring the heap property...")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child :
                print("swapping {} with {}".format(child, parent))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
                print("Heap Restored {}".format(self.heap_list))
            idx = self.parent_idx(idx)

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None
        min = self.heap_list[1]
        print("Removing: {} from {}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        print("Last element moved to the first: {}".format(self.heap_list))
        self.heapify_down()
        return min

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]
        if right_child > left_child:
            print("Left child: {}(index:{}) is smaller than Right child: {}(index:{}).".format(left_child, self.left_child_idx(idx), right_child, self.right_child_idx(idx)))
            return self.left_child_idx(idx)
        else:
            print("Right child: {}(index:{}) is smaller than Left child: {}(index:{}).".format(left_child, self.left_child_idx(idx), right_child, self.right_child_idx(idx)))
            return self.right_child_idx(idx)

    def child_present(self, idx):
        # Helper Method
        return self.left_child_idx(idx) <= self.count

    def heapify_down(self):
        print("Heapify down!")
        idx = 1
        while self.child_present(idx):
            print("Heapifying down!")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child :
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx
        print("Heap Restored! {}.".format(self.heap_list))

### CLASS INSTANTIATION---------------------
min_heap = MinHeap()

# Populate min_heap with 15 random numbers
#random_nums = [randrange(1, 101) for n in range(6)]
#for num in random_nums:
#  min_heap.add(num)

#print(min_heap.heap_list)
#print(min_heap.retrieve_min())
#print(min_heap.get_smaller_child_idx(1))
#print(min_heap.heap_list)

# Documentation Test
elements_to_add = [10, 11, 21, 12, 22, 23, 99, 61, 13]
for element in elements_to_add:
    min_heap.add(element)

print(min_heap.heap_list)
min = min_heap.retrieve_min()
