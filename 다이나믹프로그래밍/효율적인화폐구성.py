#226p

N,M= map(int,input().split())

d=[987654321]*(10001)
coins=[]
for i in range(1,N+1):
    temp=int(input())
    d[temp]=1
    coins.append(temp)

for i in range(1,M+1):
    for coin in coins:
        if i-coin>=1:
            d[i]=min(d[i-coin]+1,d[i])
             
if d[M]==987654321:
    print("-1")
else:
    print(d[M])
     
