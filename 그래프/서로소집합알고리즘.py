import heapq
import sys
input=sys.stdin.readline

#마지막에 겟페런트 한번 더돌리는게 중요함, 그래야 모든 루트값이 넣어짐
#마지막에 겟페런트 한번 더돌리는게 중요함, 그래야 모든 루트값이 넣어짐
#마지막에 겟페런트 한번 더돌리는게 중요함, 그래야 모든 루트값이 넣어짐

#부모배열 

#부모찾기
def getParent(x):
    if x!=parent[x]:
        parent[x]=getParent(parent[x])
    return parent[x]



#두원소가 속한 집합 합치기
def union(a,b):
   
    parentA=getParent(a)
    parentB=getParent(b)
    if a==2 and b==4:
        print(parentA,parentB)
        print(parentA,parentB)
    if parentA<parentB:
        parent[b]=parentA
    elif parentB < parentA:
        parent[a]=parentB


N,E=map(int,input().split())
 
parent=[0]*(N+1)
#부모배열 초기화
for i in range(1,N+1):
    parent[i]=i

for i in range(E):
    a,b=map(int,input().split())
    union(a,b)
    
#겟페런트 한번 더돌리는게 중요함, 그래야 모든 루트값이 넣어짐
for i in range(1, N+1):
    print(getParent(i))
