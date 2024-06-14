import heapq

q = [2,1,3,4,5,6]
heapq.heapify(q)

print(heapq.heappop(q))

heapq.heappush(q,-1)
print(heapq.heappop(q))

