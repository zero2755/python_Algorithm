#인덱스 에러 왜??

from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]



N,M=map(int, input().split())



graph=[]
temp = [[0] * M for _ in range(N)]


for _ in range(N):
    graph.append(list(map(int, input().split())))

result=0

def getScore():
    score=0
    for i in range(N):
        for j in range(N):
            if temp[i][j]==0:
                score+=1
    return score




def virus(x,y):
    q=deque()
    q.append((x,y))
    while q:
         
        curX,curY=q.popleft()

        for i in range(4):
            nx=curX+dx[i]
            ny=curY+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if temp[nx][ny]==0:
                    temp[nx][ny]=2
                    q.append((nx,ny))
        



def dfs(count):
    
    global result
    
    if count==3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j]==2:
                    virus(i,j)
        #print(result)
        result=max(result,getScore())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j]==0:
                 
                
                graph[i][j]=1
                count+=1
                dfs(count)
                graph[i][j]=0
                count-=1
   
dfs(0)

print(result)
 
