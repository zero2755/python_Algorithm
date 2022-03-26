N,M,K,X = map(int,input().split())

graph=[[] for _ in range(N+1)]

ansMap=[]

costMap=[987654321]*(N+1)
costMap[X]=0
for _ in range(M):
    A,B=map(int,input().split())
    graph[A].append(B)

def dfs(now,cost):

    if cost==K:
         
        return
    
    for to in graph[now]:
        if cost+1<costMap[to]:
          
            costMap[to]=cost+1
            if cost+1 > K:
                continue
            dfs(to,cost+1)


dfs(X,0)

for i in range(1,N+1):
    if costMap[i]==K:
        ansMap.append(i)
       

 

if len(ansMap)!=0:
    for i in ansMap:
        print(i)
else:
    print("-1")
    
     
