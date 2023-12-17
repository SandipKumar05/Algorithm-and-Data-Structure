## Stack using list, no need of seprate stack
a=[]
a.append(1)
a.append(2)
a.pop() # 2 get removed
print(a) #[1]

## Queue in python
from collections import deque
my_queue = deque()
# Enqueue elements, Append add element to right
my_queue.append(1) #[1]
my_queue.append(2) #[1,2]
my_queue.append(3) #[1,2,3]
# Append element to left
my_queue.appendleft(4) #[4,1,2,3]

# Pop elements from the right
item1 = my_queue.pop() #3
item2 = my_queue.pop() #2
print(item1, item2)

# Dequeue elements
item1 = my_queue.popleft() #1; 
item2 = my_queue.popleft() #2
print(item1, item2)

# this queue is min heap
from queue import PriorityQueue
print("PriorityQueue")
pq=PriorityQueue()
pq.put(1);pq.put(4);pq.put(2)
i=pq.get();j=pq.get();k=pq.get()
print(i,j,k)

# Using heapq is good option for min heap as well
import heapq
print("heapq")
l=[2,1,4]
heapq.heapify(l)
heapq.heappush(l,-2)
print(heapq.heappop(l))

# # multi dimention array
x = [[False for i in range(10)] for j in range(10)]
print(x[0][0])

# set in python
a = set()
a.add(1);a.add(1)
print(len(a))

## file manupulation 
# Read json file
print('json file')
import json
with open('example.json','r') as json_file:
    json_data=json.loads(json_file)
    print(json_data)