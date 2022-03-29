import heapq
import sys
input=sys.stdin.readline
N,M= map(int,input().split())
INF=987654321
distance=[INF]*(N+1)
visited=[False]*(N+1)
maxValue=-4

graph=[[] for _ in range(N+1)]

for _ in range(M):
    fro,to=map(int,input().split())
    graph[fro].append(to)
    graph[to].append(fro)

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if now==5:
            print("z")
        if visited[now]==False:
            visited[now]=True
            for i in graph[now]:
              cost=dist+1
              if cost<distance[i]:
                distance[i]=cost
                heapq.heappush(q,(cost,i))

dijkstra(1)
#최소헛간번호, 거리 그 헛간과 같은거리를 갖는 헛간의 개수출력 
hN=0


#맥스벨류=헛간거리


hCnt=0
#같은거리 헛간개수출력
for i in range(1,N+1):
    
    if maxValue<distance[i]:
        hN=i
        hCnt=1
        maxValue=distance[i]
    elif maxValue==distance[i]:
        
        hCnt+=1
print(hN,maxValue,hCnt)
