n=int(input())
m=int(input())

graph=[[0]*n for _ in range(n)]


num=2
cnt=1
row, col=0,-1
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x=(n-1)//2
y=(n-1)//2
#print(x,y)

ans=[x+1,y+1]
graph[x][y]=1
len=0
print(x,y,3333)
while True:
    for i in range(4):
        print(x,y)
        for _ in range(len):
            print(len)
            print(x,y,i,num)
            x+=dx[i]
            y+=dy[i]
            print(x,y)
            graph[x][y]=num
            num+=1
            if num==m:
                ans=[x+1,y+1]
    if x==y==0:
        break
    x-=1
    y-=1
    len+=2

for i in range(n):
    print(*graph[i])
print(ans)