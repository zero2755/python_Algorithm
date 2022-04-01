#디버깅용, parent를 조회하면 들어가야하는건맞는데, result에 들어간 갯수와 순서가 이상함

import heapq
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

#부모배열
parent=[0]*(N+1)
for i in range(1,N+1):
    parent[i]=i

def union(a,b):
    pA=find_parent(a)
    pB=find_parent(b)
    if pA<pB:
        parent[b]=pA
    else:
        parent[a]=pB

#부모찾기
def find_parent(x):

    if x !=parent[x]:
        parent[x]=find_parent(parent[x])
    return parent[x]


edges=[]

for i in range(M):
    a,b,c=map(int,input().split())              
    edges.append((a,b,c))

edges.sort(key=lambda x:x[2])

result=[]
for edge in edges:
     
    if find_parent(edge[0])==find_parent(edge[1]):
        print("첫엣지",edge)
else:

    print(edge)
    if edge[0]==4 and edge[1]==5:
        print("zx")
    union(edge[0],edge[1])
    result.append(edge[2])
print(parent)
 

ans=0
for x in range(len(result)-1):
    ans+=result[x]

print(ans)
 
