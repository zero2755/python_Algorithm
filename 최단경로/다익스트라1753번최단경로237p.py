# 각 정점을 돌면서 방문하지않은것중 가장 최단거리인 노드를 방문해서
# 디스탄스를 갱신시켜간다
# 70%에서틀림 간단한 구현버전임 우선순위큐 활용으로 바꿔야함
V, E =map(int,input().split())
 
K=int(input())

graph=[ [] for _ in range(V+1)]

visited=[False] * (V+1)

distance=[987654321]*(V+1)

for x in range(1,E+1):
    fro,to,cost=map(int,input().split())
    graph[fro].append((to,cost))

#현재 노드중 가장 거리가 짧은 노드를 리턴해주는
def getShortNode():
     
    smCursor=987654321
    minDistance=987654321
    for i in range(1,V+1):
        if visited[i]==True:
            continue
        if minDistance>distance[i] and distance[i] !=0:
          minDistance=distance[i]
          smCursor=i
         
    return smCursor


def dix(start):
    
    visited[start]=True
    for x in graph[start]:
        distance[x[0]]=x[1]
    distance[start]=0
    
    while True:
        now=getShortNode()
        if 987654321==now:
            break
        if visited[now] != True:
           visited[now]=True
           
           if len(graph[now])!=0:
               for x in graph[now]:
                   if distance[x[0]]>distance[now]+x[1]:
                       distance[x[0]]=distance[now]+x[1]
        else:
            break
    #now를 거쳐가면서 ditance 갱신

dix(K)

for td in range(1,V+1):
    if distance[td]==987654321:
        print("INF")
    else:
        print(distance[td])

#print("z")
