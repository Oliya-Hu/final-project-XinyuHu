from priority_queues import PriorityQueue
import time
import matplotlib.pyplot as plt

##
# Create a heap and insert some elements
heap = PriorityQueue()
for i in range(1000):
    heap.insert(i)

# Measure the execution time of delMin()
start_time = time.perf_counter()
while heap.size() > 0:
    heap.delMin()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f'delMin() took {elapsed_time:.6f} seconds to complete')



##
# Create a list of the number of elements in the heap
num_elements = [i for i in range(0,30)]

# Create a list of execution times for each number of elements
times = []
for num in num_elements:
    heap = PriorityQueue()
    for i in range(num):
        heap.insert(i)
    start_time = time.perf_counter()
    while heap.size() > 0:
        heap.delMin()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)

# Plot the results
plt.plot(num_elements,times)
plt.xlabel('Number of elements')
plt.ylabel('Execution time (seconds)')
plt.title('Performance of delMin()')
plt.show()

##
# Create a list of the number of elements in the heap
num_elements = [i for i in range(0,30)]

# Create a list of execution times for each number of elements
times = []
for num in num_elements:
    heap = PriorityQueue()
    start_time = time.perf_counter()
    for i in range(num):
        heap.insert(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)

# Plot the results
plt.plot(num_elements,times)
plt.xlabel('Number of elements')
plt.ylabel('Execution time (seconds)')
plt.title('Performance of insert()')
plt.show()


##
def benchmark(function, input_size, repeat=100):
    start = time.time()
    for _ in range(repeat):
        function(input_size)
    end = time.time()
    elapsed_time = end - start
    return elapsed_time / repeat

def test_function(n):
    # Create a new priority queue instance
    pq = PriorityQueue()
    # Insert n elements into the priority queue
    for i in range(n):
        pq.insert(i)

input_sizes = [20,30,40,50,60,70,80]
times = []
for size in input_sizes:
    elapsed_time = benchmark(test_function, size)
    times.append(elapsed_time)

# Plot the results using a library such as matplotlib
plt.plot(input_sizes, times, label='Insert')
plt.xlabel('Number of elements')
plt.ylabel('Execution time (seconds)')
plt.title('Performance of insert()')
plt.show()