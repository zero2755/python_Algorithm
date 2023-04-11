from collections import deque
import heapq


babySize=2 #물고기 크기

# 크기타음녀 못먹고 지나가고 크기 크면 그냥못지나감 작으면 먹을수잇음
# 가깝고 0,0에 가까운 물고기를 먹으려고함
#n크기일때 물고기를 N마리먹으면 크기가1커진다


N = int(input())

graph=[]

for _ in range(N):
    graph.append(list(map(int,input().split())))

costGraph=[ [0]* N for _ in range(N)]

#print(costGraph)

#bfs로 물고기 탐색함수, 탐색성공시 먹을수있는 물고기를 큐에넣는함수 호출
#먹을수있는 물고기를 큐에 넣는함수


babySize=2
eatCnt=0


# 물고기 진화 함수
def getGrow(curSize,curEatCnt):
    global babySize
    global eatCnt

    if curSize==curEatCnt:
        babySize+=1
        eatCnt=0
    else:
        eatCnt = curEatCnt #파라미터 넣어줄때 +1할예정

    #print("겟그로우",babySize,eatCnt)



ANSWER=0

#최단거리라 함은 현재 위치에서 가장 코스트(거리및시간)이 적게드는 거리 , 어차피 자기가 갈수있는곳을 모두 다 가야한다
#물고가 죽는경우 => 온 맵에 자기가 먹을수있는 물고기가 없을때
#먹을물고기를 고르고 해당 자리에갔을때 그 지점을 기준으로 다시 bfs임 그럼 bfs에 대해서 코스트 맵과 x,y정보가있어야하고 한번의 bfs가끝나면 그롤벌한 x,y를 업데이트해주고 다시 bfs수행해야함

isDie=False


def getAbsLoc(x,y):
    return abs(x+y)






#코스트가 1인 bfs니까 매번 코스트맵 초기화 하면서 힙큐로 우선순위인 위치 갱신시키면됨
def bfs(x,y):
    q=deque()
    global babySize
    global eatCnt
    global isDie
    global absX
    global absY
    global ANSWER

    isDie=True
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    hq = []

    q.append((x,y))
    #print(q)


    costGraph = [[0] * N for _ in range(N)]


    #print("아기사이즈", babySize,x,y)
    # print(graph)
    # print("구분자")
    # print(costGraph)
    while q:

        curx,cury=q.popleft()

        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            # if (nx==3) and (ny==1) and ANSWER==9:
            #
            #     print("z")
            if nx >= 0 and nx < N and ny >= 0 and ny < N:  # 맵 안에서
                if absX==nx and absY==ny : continue  #bfs출발지점은 넘김
                if babySize > graph[nx][ny] and graph[nx][ny] != 0 and costGraph[nx][ny]==0:  # 아기상어 크기가 물고기보다  크면 , 처음방문시, #bfs출발지점아닐시
                    costGraph[nx][ny]=costGraph[curx][cury]+1
                    #print(absX,absY,nx,ny,"!!!")
                    #heapq.heappush(hq, (abs(absX-nx)+abs(absY-ny), nx, ny))  # 초기 위치로부터의 절대값, x낮은순,y낮은순
                    heapq.heappush(hq, (costGraph[nx][ny], nx, ny))  # 초기 위치로부터의 절대값, x낮은순,y낮은순
                    q.append((nx, ny))
                    #graph[nx][ny] = 0
                    #print("##########")
                    isDie = False
                elif graph[nx][ny]==0 and costGraph[nx][ny]==0:
                    costGraph[nx][ny]=costGraph[curx][cury]+1
                    q.append((nx, ny))
                elif babySize == graph[nx][ny] and graph[nx][ny] != 0 and costGraph[nx][ny] == 0:
                    costGraph[nx][ny] = costGraph[curx][cury] + 1
                    q.append((nx, ny))
                        #print("@@@@@@@@@@@@")

    if len(hq) > 0:
        getGrow(babySize,eatCnt+1)
        #print(hq,"힙큐확인")

        graph[absX][absY] = 0 #기존 아기상어자리
        myCost,absX,absY=heapq.heappop(hq)
        graph[absX][absY]=9 #이동 아기상어자리
        ANSWER+=myCost
        #print(dummy,absX,absY,'확인########')
        # print(graph)
        # print("구분자")
        # print(costGraph)
    else:
        zxc=3
        # print("Heap is empty")









absX,absY=0,0
for i in range(N):
    for j in range(N):
        if graph[i][j]==9:
            absX=i
            absY=j



while True:
    bfs(absX,absY)


    if isDie==True:
        break

print(ANSWER,end='')




