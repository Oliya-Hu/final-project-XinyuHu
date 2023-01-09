from priority_queues import PriorityQueue

heap = PriorityQueue()
heap_elements=[6,3,13,45,23,7,15]
for m in heap_elements :
    heap.insert(m)
heap.visualize()