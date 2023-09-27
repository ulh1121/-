from collections import deque

n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for i in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[0]*(n+1)

# print(graph)
def bfs(visited, node, target):
    cnt=0
    queue=deque()
    queue.append(node)
    visited[node]=0
    while queue:
        node=queue.popleft()

        if node==target:
            return visited[target]
        for i in graph[node]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=visited[node]+1

    return -1

print(bfs(visited,a,b))


