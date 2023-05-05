# 0<=j<i에대해서 d[i]= max(d[i],d[j]+1) 단, if array[j]<array[i]



N = int(input())


arr = list(map(int,input().split()))


arr.reverse()
#print(arr)


d=[1] * N
#print(d)
result=1
for i in range(1,N):
    for j in range(0,i):
        if arr[j]<arr[i]:
            d[i]=max(d[i],d[j]+1)
            #result=max(result,d[i])

print(N-max(d))

