from collections import deque

#위상정렬의 2가지 특이케이스
#사이클이 발생하는경우, 위상정렬의 결과가 1개가 아니라 여러가지인 경우
#이것이 아니라면 오직 하나의경우만 존재
#일반적인 위상정렬의 겨우 정확히 N개의 노드가 큐에서 출력된다, 만일 노드가 N번 나오기전에 큐가 빈다면 사이클이다
# 특정시점에 2개이상의 노드가 큐에 한꺼번에 들어갈때는 가능한 정렬결과가 여러가지라는의미 => 고유순위가없다
# 위상정렬 수행과정에서 큐에서 노드를 뽑을때 큐의 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재하는것으로 이해할수있다


T= int(input())
for _ in range(T):
    N=int(input())
    data=list(map(int,input().split()))
    #graph=[for [False]*(N+1) _ in range(N+1)]
    graph = [[False] * (N + 1) for i in range(N + 1)]
    indegree=[0]*(N+1)
    for i in range(N):
        for j in range(i+1,N):
            graph[data[i]][data[j]] = True
            indegree[data[j]]+=1
    edgeCnt=int(input())
    for i in range(edgeCnt):
        a,b=map(int,input().split())
        if graph[a][b]:
            #a가 b를 제꼇는데 트루면
            graph[a][b]=False
            graph[b][a]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[b][a]=False
            graph[a][b]=True
            indegree[a]-=1
            indegree[b]+=1

    result=[]
    q=deque()
    for i in range(1,N):
        if indegree[i]==0:
            q.append(i)

    certain= True
    cycle=False

    for i in range(N):
        if len(q)==0:
            cycle=True
            break
        if len(q)>=2:
            certain=False
            break
        now=q.popleft()
        result.append(now)
        for j in range(1,N+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()


