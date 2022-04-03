import sys
input=sys.stdin.readline
import heapq

#388p

#입력
'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''

dx=[-1,1,0,0]
dy=[0,0,-1,1]

INF=987654321
tCase=int(input())
for i in range(tCase):
    N=int(input())
    graph=[list(map(int,input().split())) for _ in range(N)]
     
    distance=[[INF]*(N) for _ in range(N)]

    q=[]

    heapq.heappush(q,(0,0,graph[0][0]))
    #x,y,코스트
    distance[0][0]=graph[0][0]

    while q:
     
        nowX,nowY,dist=heapq.heappop(q)
        #print(nowX,nowY,dist) #x,y,코스트
    #원래가장 작은 비용 x,y에대해 인접리스트를 돌면서 최소비용을 찾았는데
    #2차원 코스트를 찾을때는 상하좌우를 돌면서 가장 작은 비용에대해 최소비용을 재갱신하는..
        for i in range(4):
            curX=nowX+dx[i]
            curY=nowY+dy[i]
            if curX>=0 and curX<N and curY>=0 and curY<N:
                cost=dist+graph[curX][curY]
                if cost<distance[curX][curY]:
                    distance[curX][curY]=cost
                    heapq.heappush(q,(curX,curY,cost))
    print(distance[N-1][N-1])

 


