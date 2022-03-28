import heapq
import sys
#전보 262p
input=sys.stdin.readline

N,E,X=map(int,input().split())


#이런방식으론 내가원하는 인접리스트 못만듬
#graph=[[]*(N+1)]
#test=[0]*N 이런식으로 사용하는 거임
graph=[[] for i in range(N+1)]

INF=987654321

for _ in range(E):
    fro,to,c=map(int,input().split())
    graph[fro].append((to,c))

visited=[False]*(N+1)
distance=[INF]*(N+1)

distX=0
distK=0

def dijk(start):
     q=[]
     heapq.heappush(q,(0,start))
     distance[start]=0
     while q:
         dist,now= heapq.heappop(q)
         if visited[now]==False:
             visited[now]=True
             for i in graph[now]:
                  
                 cost=dist+i[1]
                 if cost<distance[i[0]]:
                     distance[i[0]]=cost
                     heapq.heappush(q,(cost,i[0]))
ansCnt=0
ansTime=0
dijk(X)

for y in distance:
    print(y)

for x in distance:
    if x!=0 and x!=INF:
        ansCnt+=1
        if ansTime<x:
            ansTime=x

print(ansCnt,ansTime)
    

     

