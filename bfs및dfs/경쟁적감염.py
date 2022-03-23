N,K= map(int, input().split())

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]












'''
잘못짠구현
graph= []

for _ in range(N):
    graph.append(list(map(int, input().split())))


coin=[[] for _ in range(K+1)]

for i in range(N):
    for j in range(N):
        cur=graph[i][j]
        if cur !=0:
            coin[cur].append((i,j))


#print(coin)
#print(len(coin[0]))
S,X,Y=  map(int, input().split())              

q=deque()

#각코인마다 그 코인의 길이가 0이 아니면 bfs
q.append((1,1))


for data in coin:
    if len(data)!=0:
        print(data)
        for x in data:
            if graph[x[0]][x[1]]!=0:
               
                for i in range(4):
                    nx=x[0]+dx[i]
                    ny=x[1]+dy[i]
                    if nx>=0 and nx<N and ny>=0 and ny<N and graph[nx][ny]==0:
                        graph[nx][ny]=graph[x[0]][x[1]]
                        q.append((nx,ny))
'''


 
                     






#print("z")

