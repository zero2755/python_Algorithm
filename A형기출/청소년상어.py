
#상어는 17로

# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]
fishMap=[[0,0]  for _ in range(17)]
for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1] #주어진번호 -1 (인덱스써야하니까)
        fishNum=array[i][j][0]  #물고기번호선택
        fishCursor = array[i][j][1]  # 물고기 방향선택
        fishMap[fishNum]=[i,j,fishCursor]  #해당물고기 번호에대한 위치값 , 방향

print(array)

# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# print(array[0][0])
# print(array[0][0][0])
# print(array[0][0][1])

#fishMap=[[0,0]  for _ in range(17)]
#print(fishMap)

# for i in range(4):
#     for j in range(4):
#         fishNum=array[i][j][0]
#         fishMap[fishNum]=[i,j]

print(fishMap)

def swapFish(f1, f2): #피쉬번호1, 피쉬번호 2
    x1,y1,c1=fishMap[f1]
    x2, y2, c2 = tuple(fishMap[f1])
    print("전 , : ",fishMap[f1],fishMap[f2])
    fishMap[f1]=fishMap[f2]
    fishMap[f2]=[x1,y1,c1]

    print("후 , : ", fishMap[f1], fishMap[f2],x2,y2,c2) # => x2,y2,c2지금 이게 참조에의한복사가 되어버리는데..?


def moveFish(fishNum):
    #번호는 자동으로 순서대로 들어올거임
    #fishMap[fishNum][0],fishMap[fishNum][0],fishMap[fishNum][3] #x좌표
    x,y,curSor=fishMap[fishNum]
    print(x,y,curSor)

    #for문
    # 물고기가 가고자하는 방향이 범위 안이고 이동할수있는(상어가아닌지)지 위치 리턴받기 -> 이동할x,y 물고기 x,y,1값,빈칸x,y,2,이동할수없을때 -1,-1,3
    for i in range(8):
        curSor=(curSor+i)%8
        nx,ny,nCurSor=canMove(x,y,curSor)
        if nCurSor==3: #이동불가
            continue
        elif nCurSor==1 : #물고기서로 교환
            #물고기스왑  -> 지금물고기, 교환할물고기번호 필요
            a=3
        else: #빈칸일때 물고기만 이동
            print("zz")

    # 이동할수 없으면 방향을 꺽는다(제자리올때까지)

def canMove(x,y,curSor):
    #물고기가 가고자하는 방향이 범위 안이고 이동할수있는(상어가아닌지)지

    nx,ny=x+dx[curSor],y+dy[curSor]
    if nx>=0 and nx<4 and ny>=0 and ny <4:
        if array[nx][ny][0]==0:
            return nx,ny,2  #빈칸일때
        elif array[nx][ny]!=17: #상어가아닌 물고기일때
            return nx,ny,1
    else:
        return -1,-1,3 #이동불가

    print("z")

moveFish(1)
swapFish(1,2)
print(array)





