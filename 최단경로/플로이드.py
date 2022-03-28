import heapq
import sys
#385P 플로이드
input=sys.stdin.readline
 
INF=987654321

n=int(input())
m=int(input())


graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    fro,to,c=map(int,input().split())

    graph[fro][to]=min(graph[fro][to],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    ztr=''
    for j in range(1,n+1):
        ztr+=str(graph[i][j])+' '
    #ztr.rstrip()
    print(ztr)
        



     
