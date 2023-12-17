
x=3
y=4.3
z="abcd"

print(z+str(x))

# def finddul(a):
#     a.sort()
#     prev=0
#     nex=1
#     result=[]
#     while nex != len(a):
#         if a[prev] == a[nex]:
import math
def getTrappedRainWater(arr):
  # Write your code here
  sum=0
  n=len(arr)
  for i in range(1,n-1):
    print(arr[0:i])
    left=max(arr[0:i])
    print(left)
    print(arr[i+1:n])
    right=max(arr[i+1:n])
    print(right)
    tmp=min(left,right)-arr[i]
    if tmp>0:
      sum+=tmp
  return sum

# a = [1,2,3,1,2,3]
# a.sort()
# print(getTrappedRainWater([7,4,0,9]))

def getSmallestClockAngle(timeString, unit):
  # Write your code here
  h,m=timeString.split(":")
  h_angle=(360/12)*h
  m_andle=(360/60)*m
  
  diff=abs(h_angle,m_andle)
  if diff>180:
    diff=360-diff
  if unit == 'radians':
    diff=2*math.pi*diff/360
  return diff

import queue
class LRUCache: 
  
  size=0
  d =dict()
  q = queue.Queue() 
  def __init__(self, capacity):
    self.size=capacity
    self.q = queue.Queue(capacity)
  
  def get(self, x):
    if x in self.d:
      self.q.get(x) # Dequeue
      self.q.put(x) # Enqueue
      return self.d[x]
    return -1 

  def set(self, x, y):
    if self.q.full():
        i=self.q.get()
        del self.d[i]
        self.q.put(x)
        self.d[x]=y
    else:
        self.d[x]=y
        self.q.put(x)
    return 1

# if __name__ == "__main__":
# #   cacheOne = LRUCache(2) 
# #   cacheOne.set(1, 2)
# #   outputOne = [cacheOne.get(1)]
# #   print([2], outputOne)

#   cacheTwo = LRUCache(2)
#   cacheTwo.set(1,2)
#   print(cacheTwo.d,list(cacheTwo.q))
#   cacheTwo.set(2,3)
#   print(cacheTwo.d,list(cacheTwo.q))
#   cacheTwo.set(1,5)
#   print(cacheTwo.d,list(cacheTwo.q))
#   cacheTwo.set(4,5)
#   print(cacheTwo.d,list(cacheTwo.q))
#   cacheTwo.set(6,7)
#   print(cacheTwo.d,list(cacheTwo.q))
#   outputTwo = [cacheTwo.get(4)]
#   print(cacheTwo.d,list(cacheTwo.q))
#   cacheTwo.set(1,2)
#   print(cacheTwo.d,list(cacheTwo.q))
#   outputTwo.append(cacheTwo.get(3))
#   print([5, -1], outputTwo)


# def gameScoring(score):
#   # Write your code here
#   s = queue.LifoQueue()
#   result=[]
#   s.put([1])
#   s.put([2])
#   s.put([3])
#   while not s.empty():
#     i = s.get()
#     print(i)
#     sum_ = sum(i)
#     if sum_ == score:
#       result.append(i)
#     elif sum_ > score:
#         continue
#     else:
#       for j in [1,2,3]:
#         s.put(i+[j])
#   return result

# print(gameScoring(3))

f = open('rank.csv')
# a=f.readline()
# a=a.replace('\n', '')
# print(a.split('\t'))

for line in f.readlines():
    # print(line)
    a=line.replace('\n', '')
    data=a.split('\t')
    rank=int(data[6])
    # print(data[4])
    if rank > 100000:
        if 'Female' not in data[4]:
            print(line)