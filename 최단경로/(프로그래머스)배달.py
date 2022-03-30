import sys
import heapq
INF=987654321
    #배달
    #나는 힙큐그래프 초기화할때 양방향이면 fro to 바꿔서 한번더해야하는데 그걸 
    #자꾸 까먹음
    #https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    #print(N)
    print(road)
    #print(K)
 
    
    #road
    #fro, to, cost
    #일단 이걸 인접리스트로바꾸자
    road.sort()
    
    graph=[[] for _ in range(N+1)]
    for x in road:
        graph[x[0]].append((x[1],x[2]))
        graph[x[1]].append((x[0],x[2]))
    distance=[INF]*(N+1)
    visited=[False]*(N+1)
    q=[]
    #print(road[0])
    distance[1]=0
    heapq.heappush(q,(0,1))
    while q:
        dist,now=heapq.heappop(q)
        visited[now]=True
        for i in graph[now]:
            
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
        
        
    print(distance)    
        
    
    
    '''
    마을갯수만큼 다익스트라 배열만들고 로드를돌면서
    '''
    #K보다 같거나작으면 cnt+=1
    answer = 0
    for i in distance:
        if i<=K:
            answer+=1
    

   
    return answer
