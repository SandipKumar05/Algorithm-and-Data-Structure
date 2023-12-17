import queue
def dfs(i,j,visited):
    rm=[-1,1,0,0]
    cm=[0,0,-1,1]
    s = queue.LifoQueue()
    s.put((i,j))
    while not s.empty():
        r,c = s.get()
        for k in range(len(rm)):
            ti=r+rm[k]
            tj=c+cm[k]
            if ti>=0 and ti<row and tj>=0 and tj<col and not visited[ti][tj] and mat[ti][tj]==1:
                s.put((ti,tj))
                visited[ti][tj]=True
                print('hello')


def islands():
    count=0
    # global visited
    visited=[[False for j in range(col)] for i in range(row)]

    for i in range(row):
        for j in range(col):
            if not visited[i][j] and mat[i][j]==1:
                dfs(i,j,visited)
                print(visited)
                count+=1
    return count

mat=[[1,1,0,0,0],
     [0,1,0,0,1],
     [1,0,0,1,1],
     [0,0,0,0,0],
     [1,0,1,0,1]]
row=len(mat)
col=len(mat[0])
r,c=(1,2)

print(islands())

def test(visited):
    visited[0][0]=True

def t():
    visited=[[False for j in range(col)] for i in range(row)]
    test(visited)
    print(visited)
t()