n=int(input())
m=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
parents=list(range(n))
plan=list(map(int,input().split()))

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)

    if x>y:
        parents[x]=y
    else:
        parents[y]=x

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j]==1:
            union(i,j)
print(parents)
ans="YES"
for i in range(1,m):
    if parents[plan[i]-1]!=parents[plan[0]-1]:
        ans="NO"
        break
print(ans)


