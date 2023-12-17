
class node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
def maxDepth(node):
    if node == None:
        return -1
    else:
        left=maxDepth(node.left)
        right=maxDepth(node.right)
        return left+1 if left>right else right+1

def isIdentical(t1,t2):
    if t1 == None and t2 == None:
        return True
    if t1.data == t2.data:
        return isIdentical(t1.left,t2.left) and isIdentical(t1.right,t2.right)
    return False

def isMirriorTree(t1,t2):
    if t1 == None and t2 == None:
        return True
    if t1.data == t2.data:
        return isMirriorTree(t1.left,t2.right) and isMirriorTree(t1.right,t2.left)
def isMirrior(root):
    if root == None:
        return True
    return isMirriorTree(root.left,root.right)
    
# max defference between two nodes
def diameter(root):
    if root == None:
        return 0
    left_depth=maxDepth(root.left)
    right_depth=maxDepth(root.right)
    l_d = diameter(root.left)
    r_d = diameter(root.right)
    return max(l_d,r_d,left_depth+right_depth+1)

import queue
def level_avg(root):
    q = queue.Queue()
    result=[]
    q.put(root)
    while not q.empty():
        size=q.qsize()
        sum=0
        for i in range(size):
            n=q.get()
            sum+=n.data
            if n.left != None:
                q.put(n.left)
            if n.right != None:
                q.put(n.right)
        avg=sum/size
        result.append(avg)
    return result
root=node(1)
root.left=node(2)
root.right=node(5)
root.left.left=node(3)
root.left.left.right=node(3)
print(level_avg(root))
'''
1
2 5
 3
  3
'''