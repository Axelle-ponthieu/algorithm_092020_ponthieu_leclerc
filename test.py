
 
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
class FibonacciHeap:
    def __init__(self):
        self.heap = []
        self.mini = None
        self.count = 0
 
    def insert(self, value):
        new_node = Node(value)
        self.heap.append(new_node)
        if (self.mini is None or value < self.mini.value):
            self.mini = new_node
        self.count = self.count + 1
 
    def find_min(self):
        if self.mini is None:
            return None
        return self.mini.value
 
    def delete_min(self):
        smallest = self.mini
        if smallest != None:
            for child in smallest.children:
                self.heap.append(child)
            self.heap.remove(smallest)
            if self.heap == []:
                self.mini = None
            else:
                self.mini = self.heap[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.key
 
#     def consolidate(self):
#         aux = (floor_log2(self.count) + 1)*[None]
 
#         while self.trees != []:
#             x = self.trees[0]
#             order = x.order
#             self.trees.remove(x)
#             while aux[order] is not None:
#                 y = aux[order]
#                 if x.key > y.key:
#                     x, y = y, x
#                 x.add_at_end(y)
#                 aux[order] = None
#                 order = order + 1
#             aux[order] = x
 
#         self.least = None
#         for k in aux:
#             if k is not None:
#                 self.trees.append(k)
#                 if (self.least is None
#                     or k.key < self.least.key):
#                     self.least = k
 
 
# def floor_log2(x):
#     return math.frexp(x)[1] - 1
 
 
fheap = FibonacciHeap()
 
print('Menu')
print('insert <data>')
print('min get')
print('min extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        fheap.insert(data)
    elif operation == 'min':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Minimum value: {}'.format(fheap.find_min()))
        elif suboperation == 'extract':
            print('Minimum value removed: {}'.format(fheap.delete_min()))
 
    elif operation == 'quit':
        break

    