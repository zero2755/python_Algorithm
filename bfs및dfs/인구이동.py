from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]
N,L,R=map(int,input().split())
graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))
q=deque()

def canUnion(x,y,nx,ny):
    if L<=abs(graph[x][y]-graph[nx][ny])<=R:
        return True
    else:
        return False
    
visited=[[0] * N for _ in range(N)]
 

def bfs(x,y):
    global toggle
    toggle=False
    q.append((x,y))
    tSum=graph[x][y]
    visited[x][y]=1
    unionMap=[]
    unionMap.append((x,y)) #각연합 맵지도
    unionCnt=1  #유니온갯수
    while q:
        x,y=q.popleft()
        visited[x][y]=1
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
                
            if nx>=0 and nx<N and ny>=0 and ny<N:
                if canUnion(x,y,nx,ny) and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    toggle=True #이동할여지가있음=> cnt증가 가능
                    tSum+=graph[nx][ny] #연합의 인구합
                    unionMap.append((nx,ny)) #연합목록
                    unionCnt+=1 #연합갯수
                    visited[nx][ny]=1 #방문처리
                    q.append((nx,ny)) #큐에넣음
    
    unionResult =tSum//unionCnt

    for x in unionMap:
        graph[x[0]][x[1]]=unionResult


ans=0              
toggle=True
while toggle:
    visited=[[0] * N for _ in range(N)]
    tempToggle=False
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                 
                bfs(i,j)
                if toggle==True:
                     
                    tempToggle=True
    if tempToggle==True:
        ans+=1
        toggle=True


print(ans)


