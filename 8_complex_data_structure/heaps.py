class MinHeap():
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def add(self, element):
        print("\nAdding {element} to {heap_list}.".format(element = element, heap_list = self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring the heap property...")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                print("swapping {} with {}".format(parent, child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {}".format(self.heap_list))

    def retrieve_min(self):
        if self.count == 0:
            print("No items in the heap")
            return None
        min = self.heap_list[1]
        print("Removing: {} from {}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count =- 1 
        print("Last element moved to the first: {}".format(self.heap_list))
        self.heapify_down()
        return min

    def heapify_down(self):
        print("Heapify down!")
        idx = 1

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child > right_child:
                return self.right_child_idx(idx)
            else:
                return self.left_child_idx(idx)
        else:
            print("There is only a left child")
            return self.left_child_idx(idx)

    def parent_idx(self, idx):
        # Helper Method
        return idx // 2

    def left_child_idx(self, idx):
        # Helper Method
        return idx * 2

    def right_child_idx(self, idx):
        # Helper Method
        return idx * 2 + 1

    def display_parent(self, index):
        index_value = self.heap_list[index]
        if index == 1:
            print("{index_value} (index: {index}) is the root.".format(index = index, index_value = index_value))
        else:
            index_parent = self.parent_idx(index)
            value_parent = self.heap_list[index_parent]
            print("{index_value} (index: {index}) parent is : {value_parent} (index: {index_parent})".format(index = index, index_value = index_value, index_parent = index_parent, value_parent = value_parent))

    def display_child(self, index):
        index_value = self.heap_list[index]
        if (len(self.heap_list) < index * 2 + 1) or (len(self.heap_list) < index * 2):
            print("{index_value} (index: {index}) has no child.".format(index = index, index_value = index_value))
        else: 
            index_l_child = self.left_child_idx(index)
            value_l_child = self.heap_list[index_l_child]
            index_r_child = self.right_child_idx(index)
            value_r_child = self.heap_list[index_r_child]
            print("{index_value} (index: {index}) has left child : {value_l_child} (index: {index_l_child}) and right child : {value_r_child} (index: {index_r_child})".format(index = index, index_value = index_value, index_l_child = index_l_child, value_l_child = value_l_child, index_r_child = index_r_child, value_r_child = value_r_child))
 
min_heap = MinHeap()

min_heap.add(10)
min_heap.add(13)
min_heap.add(21)
min_heap.add(61)
min_heap.add(22)
min_heap.add(23)
min_heap.add(99)
min_heap.add(12)
min_heap.add(11)

print("\nHeap List has {} elements".format(min_heap.count))
print(min_heap.heap_list)

print("\nPrint Heap Parents")
for i in range(1,len(min_heap.heap_list)):
    min_heap.display_parent(i)

print("\nPrint Heap Childs")
for i in range(1, len(min_heap.heap_list)):
    min_heap.display_child(i)

min = min_heap.retrieve_min()
print("Min: {} has been retrieved from heap.".format(min))

print("\nThe smaller child of index 1: ")
smaller_child_idx_1 = min_heap.get_smaller_child_idx(1)
print(smaller_child_idx_1)

print("\nThe smaller child of index 2: ")
smaller_child_idx_2 = min_heap.get_smaller_child_idx(2)
print(smaller_child_idx_2)

print("\nThe smaller child of index 3: ")
smaller_child_idx_3 = min_heap.get_smaller_child_idx(3)
print(smaller_child_idx_3)


