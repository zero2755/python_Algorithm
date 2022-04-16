from bisect import bisect_left
idx1=0 #없으며 ㄴ인덱스는?

inArr=[2,3,1,2,2]

idx1=bisect_left(inArr,0)
print(idx1)
inArr.sort()

#1,2,2,2,3
Ans=0
curLv=1
curCnt=0

for i in range(len(inArr)):
    if 1 == inArr[i]:
        Ans+=1
        tempNum=1
        continue
    #2,2,2 이렇게올때 2,2면 ans+1하고 curCnt초기화해줘야함
    if tempNum == inArr[i]:
        curCnt+=1
        if tempNum==curCnt:
            Ans+=1
            curCnt=0

    if tempNum!=inArr[i]:

        if curCnt>0:

            break
        curCnt += 1


    tempNum=inArr[i]#이전 숫자 비교위함

print(Ans)
