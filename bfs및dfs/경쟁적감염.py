#다시
N,K= map(int, input().split())

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]


graph= []

data=[]

#종류ㅜ 시간 위치
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))


target_S, target_X, target_Y = map(int, input().split())

q=deque(data)

while q:
    
    v,s,x,y=q.popleft()

    if s==target_S:
        print(graph[target_X-1][target_Y-1])
        break
        #print(x,y)
        #print("============")
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<N and graph[nx][ny]==0:
            graph[nx][ny]=v
            q.append((v,s+1,nx,ny))
        
        

             

