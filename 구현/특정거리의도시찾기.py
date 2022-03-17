# 왜틀린건지 디버깅필요함

from collections import deque

N,M,K,X=map(int,input().split())

graph=[[] for _ in range(N+1)]
 
 
for _ in range(M):
    node,to=map(int,input().split())
    graph[node].append(to)
queue=deque()
visited=[]
ans=[]
queue.append((X,0))
while queue:
    node,cost=queue.popleft()
     
    
    for x in graph[node]:
        if x not in visited:
            visited.append(x)
             
            if cost==(K-1):
                ans.append(str(x))
            else:
                queue.append((x,cost+1))

if len(ans)==0:
    print("-1")
else:
    for i in ans:
        print(i)
            
        


