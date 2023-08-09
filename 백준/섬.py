from collections import deque
from collections import Counter

import sys

def dfs(x,y):
    dx = [-1, 1, -1, 1, 0, 0, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    graph[x][y]=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if(nx>=0 and nx<h and nx<=0 and ny<w and graph[nx][ny]==1):
            dfs(nx,ny)


lines=sys.stdin.readline
while True:
    w,h=map(int,lines().split())
    if(w==0 and h==0):
        break
    graph=[]
    count=0
    for i in range(h):
        graph.append(list(map(int,lines().split())))

    for i in range(h):
        for j in range(w):
            if(graph[i][j]==1):
                dfs(i,j)
                count+=1
    print(count)





