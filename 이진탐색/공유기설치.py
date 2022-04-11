#공유기 설치
#2110번 , 디버깅필요 
N,C= map(int, input().split())

house=[]

for i in range(N):
    house.append(int(input()))

ans=0
house.sort()
start=house[0]
end=house[N-1]
#print(house)

while start<=end:

    mid=(start+end)//2
    cCnt=1
    tempHouse = 0  # 임시 공유기 설치장소
    tempDis=987654321987 #인접한 두 공유기 사이의 거리중 가장 짧은거
    for i in range(N-1):
        #print(i,"아이는")

        distance=house[i+1]-house[tempHouse]
        if distance<=mid:
            continue

        else:
            #print("설치장소번째",i+1)
            cCnt+=1
            tempDis = min(tempDis, distance)
            tempHouse=i+1



    #설치공유기가 너무많은경우, 길이늘려야할경우
    if cCnt>C:
        start=mid+1
        #end = mid - 1
        #print(mid,"길이 모자람, 미드를 키워야함 ")
    #길이가 넘쳐 공유기를 덜설치함
    if cCnt<C:
        end=mid-1
        #start = mid + 1
        #print(mid,"길이넘침, 미드가 너무 큼")



    if cCnt==C:
        end=mid-1

        ans=max(ans,tempDis)
    #print(ans, "<=== ans")




print(ans)
