import heapq
import sys
input=sys.stdin.readline
INF=987654321

N,M=map(int,input().split())

start=int(input())


distance=[INF]*(N+1)

graph=[ [] for _ in range(N+1)]
#print(N)
#print(graph)

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))


def dijkstra(start1):
    distance[start1] = 0
    q=[]

    heapq.heappush(q, (start,0))
    distance[start]=0
    #시작은 스타트노드 , 스타트노드를 돌면서 각 거리를 초기화시켜야한다
    while q:

        cur,cost=heapq.heappop(q)
        for x in graph[cur]:
            newOne,newOneCost=x[0],x[1]

            newCost=cost+newOneCost
            if newCost<distance[newOne]:
                distance[newOne]=newCost
                heapq.heappush(q,(newOne,newCost))







dijkstra(start)

for x in distance:
    print(x)
