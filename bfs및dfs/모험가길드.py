# 311p

N= int(input())
aList=list(map(int,input().split()))

aList.sort()
ans=0
print(aList)
temp=2
tempGroup=0
for i in range(N):
    
    if i==1:
        ans+=1
    else:
        if temp != i:
            temp=i
        tempGroup+=1
        if temp==tempGroup:
            ans+=1
            tempGroup=0
print(ans)
