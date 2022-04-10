import sys
input=sys.stdin.readline

tempGraph=[list(map(int,input().split())) for _ in range(4)]

dx=[0,-1,-1,0,1,1,1,0,-1]
dy=[0,0,-1,-1,-1,0,1,1,1]
#0은 더미, 위쪽부터 반시계방향

graph=[[] for i in range(4)]
for i in range(4):
    for j in range(0,8,2):
        graph[i].append((tempGraph[i][j],tempGraph[i][j+1]))


#mX 16개의물고기좌표 ? 죽으면 -1로
#mY
mX=[0]*17
mY=[0]*17

for i in range(4):
    curY=0
    for x in graph[i]:
        mX[x[0]]=i
        mY[x[0]]=curY
        curY+=1



#물고기이동함수 

#상어 위치초기화
sX=0
sY=0

#상어 이동함수 dfs

def dfs(a,b,sumValue):
    #방향의 끝으로이동
    #각방향에 아무것도 없을때 리턴

    dfs(a,b,sumValue+1)



dfs(0,0,graph[0][0][0])

#graph[0][0][0]=> 번호
#graph[0][0][1]=> 방향 1~8

#print(graph[0][0][0])
#print(graph)
print(graph)
