#뱀, 코딩 바꾸기위해 남겨놓음

import heapq
import sys
from collections import deque
input=sys.stdin.readline



N=int(input())
K=int(input())

graph=[[0]*(N+1) for _ in range(N+1)]

for i in range(K):
    x,y=map(int,input().split())
    graph[x][y]=1

time=0

toggle=True

curX=1

curY=1

tailX=1
tailY=1
##상하좌우 1,2,3,4
dir=4
graph[1][1]=2

L=int(input())
q=deque()

for i in range(L):
    q.append(list(map(str, input().split())))
     

qTime,qValue=q.popleft()

while toggle:
    time+=1
    
    if time==qTime:
        

    #사과로직

    if dir==1:
        curX-=1
        if curX==0 or curX>N:
            break

        if graph[curX][curY]==0:
            graph[curX][curY]=2
            graph[tailX][tailY]=0
            tailX-=1
        elif graph[curX][curY]==2:
            
            break
        else:
            graph[curX][curY]=2
    elif dir==2:
        curX+=1
        if curX==0 or curX>N:
            break

        if graph[curX][curY]==0:
            graph[curX][curY]=2
            graph[tailX][tailY]=0
            tailX+=1
        elif graph[curX][curY]==2:
            
            break
        else:
            graph[curX][curY]=2
    
    elif dir==3:
        curY-=1
        if curY==0 or curY>N:
            break

        if graph[curX][curY]==0:
            graph[curX][curY]=2
            graph[tailX][tailY]=0
            tailY-=1
        elif graph[curX][curY]==2:
            
            break
        else:
            graph[curX][curY]=2
    else:
        curY+=1
        if curY==0 or curY>N:
            break

        if graph[curX][curY]==0:
            graph[curX][curY]=2
            graph[tailX][tailY]=0
            tailY+=1
        elif graph[curX][curY]==2:
            
            break
        else:
            graph[curX][curY]=2
        
print(time)

print(graph)
