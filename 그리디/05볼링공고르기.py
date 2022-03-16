#from itertools import combinations

 

N, M = map(int,input().split())

data= list(map(int,input().split()))

myLen=len(data)

ans=0
for i in range(myLen):
    for j in range(i+1,myLen):
        if data[i]!= data[j]:
            ans+=1

print(ans)
