from collections import deque
import sys
n,m,t=map(int,input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))
    if 2 in graph[i]:
        sword = [i, graph[i].index(2)]

def bfs(x,y,target_x,target_y,time):
    q=deque([(x,y,time)])
    visited=[[0]*m for _ in range(n)]

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y,time=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1 and visited[nx][ny]==0:
                if nx==target_x and ny==target_y:
                    return time+1
                visited[nx][ny]=1
                q.append((nx,ny,time+1))
    return float('inf')

# 칼 없을 경우
ans1=bfs(0,0,n-1,m-1,0)

# 칼 쓸 경우
tmp=bfs(0,0,sword[0],sword[1],0)

if tmp!=float('inf'):
  
    ans=tmp+abs(n-1-sword[0])+abs(m-1-sword[1])
else:
    ans=tmp
ans=min(ans,ans1)
if ans<=t:
    print(ans)
else:
    print("Fail")







