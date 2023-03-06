import sys

input=sys.stdin.readline

from collections import deque
import heapq

T=int(input())

N=int(input())

INF=987654321

graph=[]


d=[]



for _ in range(N):
    graph.append(list(map(int,input().split())))
    d.append([INF]*N)

d[0][0]=0



dx=[0,0,-1,1]
dy=[1,-1,0,0]

#4방향으로 bfs하면서 다익스트라




def dij():

    q=[]
    heapq.heappush(q,(graph[0][0],0,0))


    while q:
        cost,curX,curY=heapq.heappop(q)

        for i in range(4):
            nx= curX+dx[i]
            ny= curY+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N:
                nCost=cost+graph[nx][ny]
                if nCost<d[nx][ny]:
                    d[nx][ny]=nCost
                    heapq.heappush(q,(nCost,nx,ny))




dij()

print(d)

# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 
# 5
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 
# 7 
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4



