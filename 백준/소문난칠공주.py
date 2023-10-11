from collections import deque
import sys
from itertools import combinations
input=sys.stdin.readline
graph=[]
for i in range(5):
    graph.append(list(input().rstrip()))
pos=[(i,j) for i in range(5) for j in range(5)]
combs=list(combinations(pos,7))

def cnt_S(lists):
    cnt=0
    for i,j in lists:
        if graph[i][j]=="S":
            cnt+=1
    return True if cnt>=4 else False

def bfs(combss):
    visited=[False]*7
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque()
    queue.append(combss[0])
    visited[0]=True

    while queue:
        x,y= queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx,ny) in combss:
                next_comb=combss.index((nx,ny))
                if not visited[next_comb]:
                    queue.append((nx,ny))
                    visited[next_comb]=True
    return False if False in visited else True
ans=0
for comb in combs:
    if cnt_S(comb)==True:
        if bfs(comb)==True:
            ans+=1

print(ans)