from collections import deque
from collections import Counter
m,n,h=map(int,input().split())
graph=[]

for i in range(h):
    tmp=[]
    for j in range(n):
        tmp.append(list(map(int,input().split())))
    graph.append(tmp)
# print(graph[1][1][2])# 높이 행 열

ans=0
queue=deque()
def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x,y,z=queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if(0<=nx<h and 0<=ny<n and 0<=nz<m):
                if(graph[nx][ny][nz])==0:
                    graph[nx][ny][nz]=graph[x][y][z]+1
                    queue.append((nx,ny,nz))

    return True
for i in range(h):
    for j in range(n):
        for z in range(m):
            if graph[i][j][z]==1:
                queue.append((i,j,z))

bfs()
is0=False

for i in range(h):
    for j in range(n):
        for z in range(m):
            if(graph[i][j][z]==0):
                is0=True
            ans=max(graph[i][j][z],ans)

if is0==True:
    print(-1)
else:
    print(ans-1)

