import heapq
q=[]
N=int(input())
for i in range(N):
    heapq.heappush(q,int(input()))
count=0
while len(q)!=1:
    fi=heapq.heappop(q)
    se=heapq.heappop(q)

    sum=fi+se
    count+=sum
    heapq.heappush(q,sum)
print(count)
