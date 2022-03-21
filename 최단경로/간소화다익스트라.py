#간소화된 다익스트라 
#249p
#6 11
#1
#1 2 2
#1 3 5
#1 4 1
#2 3 3
#2 4 2
#3 2 3
#3 6 5
#4 3 3
#4 5 1
#5 3 1
#5 6 2

import heapq
import sys

input= sys.stdin.readline

INF=987654321

n,m= map(int, input().split())

start= int(input())

graph = [[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    fro, to , c =map(int,input().split())
    graph[fro].append((to,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))

    distance[start]=0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
