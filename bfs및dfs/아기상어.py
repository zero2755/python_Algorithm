#갱신지점의 시간관리 ? 
from collections import deque

#상좌하우
dx=[-1,0,1,0]
dy=[0,-1,0,1]

#물고기크기1~6배열
fishies=[0]*10

N=int(input())

#N*N배열만들기
graph=[list(map(int,input().split())) for _ in range(N)]

curLv=2
curCnt=0

#print(fishies)
#print(graph)
X,Y=0,0
for i in range(N):
    for j in range(N):
        fishies[graph[i][j]]+=1   #각 물고기 크기별 갯수 증가
        if graph[i][j]==9:
            X,Y=i,j


print(X,Y,"<=상어시작위치")

def isEnd():
    global curLv,curCnt
    print("isEnd함수")
    print(curLv,curCnt)
    print(fishies)
    for i in range(1,curLv):
        if fishies[i]!=0:
            return False    #크기1부터 현재 상어레벨까지 잡아먹을수있는게있으면 끝나지않았음 리턴
    return True

glbTime=0
ans=0
def bfs(X,Y):

    global ans,curLv,curCnt,glbTime
    q=deque()
    q.append((X,Y,0))
    endToggle=0
    while q:
        curX,curY,time=q.popleft()


        if isEnd()==True:
            print(curX,curY,time)
            ans=time
            break


        for i in range(4):
            nx=curX+dx[i]
            ny=curY+dy[i]
            if nx==0 and ny==2:
                print("z")
            if(nx>=0 and nx<N and ny>=0 and ny<N):
                if curLv>graph[nx][ny] and graph[nx][ny]!=0 and graph[nx][ny]!=9:

                    curCnt+=1
                    glbTime=time+1
                    print("확인@@@@@@@@@@@@@@@@@@@@@ ==>", nx, ny, curLv, curCnt, time, glbTime)
                    if curLv==curCnt:
                        curLv+=1
                        curCnt=0
                    fishies[graph[nx][ny]] -= 1
                    graph[nx][ny]=0
                    # 엄마에게 도움요청
                    if isEnd() == True:
                        #print(curX, curY, time)
                        ans = glbTime
                        endToggle=1
                        break

                q.append((nx,ny,glbTime))
        if endToggle==1:
            break


bfs(X,Y)
print(ans)



