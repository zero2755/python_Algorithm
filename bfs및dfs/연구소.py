import sys
input=sys.stdin.readline
import heapq
from collections import deque

N,M=map(int,input().split())

graph=[list(map(int,input().split())) for _ in range(N)]
temp=[[0]*M for _ in range(N)]

def get_Score():
    score=0
    for i in range(N):
        for j in range(N):
            if temp[i][j]==0:
                score+=1
    #print(score,"스코어")
    return score

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def virus(x,y):
    q=deque()
    q.append((x,y))
    while q:
        tx,ty=q.popleft()
        for i in range(4):
            curX=dx[i]+tx
            curY=dy[i]+ty
            if curX>=0 and curY>=0 and curX<N and curY<M:
                if temp[curX][curY]==0:
                    temp[curX][curY]=2
                    q.append((curX,curY))

ans=-1
 
def dfs(count):
    global ans,temp
    if count==3:
        #temp초기화
        temp=[[0]*M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp[i][j]=graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j]==2:
                    virus(i,j)
        ans=max(ans,get_Score())
        
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                graph[i][j]=1
                count+=1
                dfs(count)
                count-=1
                graph[i][j]=0
dfs(0)
print(ans)





