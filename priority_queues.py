import graphviz

class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class PriorityQueue:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size 

    def get_root(self):
        return self._get_node(0)
        
    def get_parent(self, i):
        if i == 0:
            return None
        return self._get_node(int((i-1)/2))

    def get_left_child(self, i):
        left_child_index = 2*i + 1
        if left_child_index >= self._size:
            return None
        return self._get_node(left_child_index)

    def get_right_child(self, i):
        right_child_index = 2*i + 2
        if right_child_index >= self._size:
            return None
        return self._get_node(right_child_index)

    def insert(self, key):
    # Add new element to the end of the queue
        new_node = Node(key)
        if self._tail is None:
            self._head = new_node
            self._tail = new_node
            self._size += 1
        else:
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1

        # Bubble up the new element
        current_index = self._size - 1
        while current_index > 0:

            current_node = self._get_node(current_index)
            parent_node = self.get_parent(current_index)

            if current_node.key < parent_node.key:
                # Swap current node and parent node
                current_node.key, parent_node.key = parent_node.key, current_node.key
                parent_index = int((current_index - 1) / 2)
                current_index = parent_index
            else:
                break


    def delMin(self):
        if self._size == 0:
            raise ValueError('Cannot delete from an empty Priority Queue')
        
        min_key = self._head.key
        
        # Swap first and last elements
        first_node = self._get_node(0)
        last_node = self._get_node(self._size - 1)
        first_node.key, last_node.key = last_node.key, first_node.key

        # Remove last element
        if self._tail == self._head:
            self._tail = None
            self._head = None
        else:
            prev_node = self._get_node(self._size - 2)
            prev_node.next = None
            self._tail = prev_node
        self._size -= 1

        # Bubble down the new first element
        current_index = 0
        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            if left_child_index >= self._size:
                # No more children, we're done
                break

            current_node = self._get_node(current_index)
            left_child_node = self._get_node(left_child_index)
            if right_child_index >= self._size:
                # Only left child exists
                if left_child_node.key < current_node.key:
                    current_node.key, left_child_node.key = left_child_node.key, current_node.key
                    current_index = left_child_index
                else:
                    break
            else:
                # Both children exist
                right_child_node = self._get_node(right_child_index)
                if left_child_node.key < current_node.key or right_child_node.key < current_node.key:
                    if left_child_node.key < right_child_node.key:
                        current_node.key, left_child_node.key = left_child_node.key, current_node.key
                        current_index = left_child_index
                    
                    else:
                        current_node.key, right_child_node.key = right_child_node.key, current_node.key
                        current_index = right_child_index

                else:
                    break
        return min_key
    

    def visualize(self):
        # Create a Graphviz graph
        graph = graphviz.Graph()

        # Add nodes for each element in the heap
        for i in range(self._size):
            node = self._get_node(i)
            graph.node(str(i), str(node.key))

        # Add edges between parent and child nodes
        for i in range(self._size):
            parent_index = int((i - 1) / 2)
            if parent_index >= 0:
                left_child_index = 2 * i + 1
                right_child_index = 2 * i + 2
                if left_child_index < self._size:
                    graph.edge(str(i), str(left_child_index))
                if right_child_index < self._size:
                    graph.edge(str(i), str(right_child_index))

        # Render and return the graph
        return graph.render(format='png')

    def _get_node(self, i) -> Node:
        if i < 0 or i >= self._size:
            raise IndexError('Out of bounds')
        cnt = 0
        walk = self._head
        while cnt < i:
            walk = walk.next
            cnt += 1
        return walk