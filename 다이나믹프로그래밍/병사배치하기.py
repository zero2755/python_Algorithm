#380p
#18353
import sys

input=sys.stdin.readline

N=int(input())

cList=list(map(int,input().split()))
cList.reverse()

dp=[1]*N

for i in range(1,N):
    for j in range(0,i):
        if cList[j]<cList[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(N-max(dp))
