class Heap(object):
   
    def insert(self, value: int) -> None:
        
        pass

    def find_min(self) -> int:
        
        pass

    def delete_min(self) -> int:
       
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        
        pass


class Node:

    def __init__(self, value):
        self.value = value
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1

class FibonacciHeap(Heap):

    heap2 = [2, 4, 5, 6]

    def __init__(self):
        self.heap = []
        self.mini = None
        self.count = 0

    def insert(self, value: int) -> None:
        new_node = Node(value)
        self.heap.append(new_node)
        if (self.mini is None or value < self.mini.value):
            self.mini = new_node
        self.count = self.count + 1

    def find_min(self) -> int:
        
        if self.mini is None: 
            return None
        return self.mini.value

    def delete_min(self) -> int:
        
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        heap2 = []
        for value in heap2:
            self.heap.append(value)

#pour tester le merge 

heap = FibonacciHeap()
heap.insert(42)

heap2 = FibonacciHeap()
heap2.insert(0)

heap.merge(heap2)


# faire une boucle insert sur la liste heap2 vers heap, avant il faut definir heap et heap2