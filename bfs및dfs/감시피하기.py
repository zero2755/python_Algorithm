from collections import deque
from itertools import permutations
from itertools import combinations
import sys
import heapq

input=sys.stdin.readline

#감시피하기 351p

N=int(input())

graph=[list(map(str,input().split())) for _ in range (N)]


temp=[['X']*N for _ in range(N)]

tLocation=[]

#선생위치입력
for i in range(N):
    for j in range(N):
        if graph[i][j]=='T':
            tLocation.append((i,j))

#선생위치에서 상하좌우로 쭉가다가 걸리면 false
def check():
    #0,2
    #1,1
    #2,2
    #if temp[0][2]=='O' and temp[1][1]=='O' and temp[2][2]=='O':
        #print("z11")
    #print("chk")
    for x in tLocation:
        #x[0],x[1]기준 상하좌우
        curX=x[0]
        curY=x[1]
        
        #상
        cnt=1
        while curX-1>=0:
            curX=x[0]-cnt
            curY=x[1]
            cnt+=1
            if curX>=0:
                if temp[curX][curY]=='O':
                    #print("1")
                    break
                if temp[curX][curY]=='S':
                    #print("5")
                    return False
        #하
        cnt=1
        curX=x[0]
        curY=x[1]
        while curX+1<N:
            curX=x[0]+cnt
            cnt+=1
            if curX<N:
                if temp[curX][curY]=='O':
                    #print("2")
                    break
                     
                if temp[curX][curY]=='S':
                    #print("6")
                    return False

        #좌
        cnt=1
        curX=x[0]
        curY=x[1]
        while curY-1>=0:
            curY=x[1]-cnt
            cnt+=1
            if curY>=0:
                if temp[curX][curY]=='O':
                    #print("3")
                    break
                if temp[curX][curY]=='S':
                    #print("7")
                    return False
        #우
        cnt=1
        curX=x[0]
        curY=x[1]
        while curY+1<N:
            curY=x[1]+cnt
            cnt+=1
            if curY<N:
                if temp[curX][curY]=='O':
                    #print("4")
                    break
                if temp[curX][curY]=='S':
                    #print("8")
                    return False
    #print("z")
    return True

ans1=False
ans2=False
def dfs(count):
    global ans1,ans2
    if count==3:
        for i in range(N):
            for j in range(N):
                temp[i][j]=graph[i][j]
        ans1=check()
        #print(ans1)
        if ans1==True:
            ans2=True
        return

    for i in range(N):
        for j in range(N):
            if graph[i][j]=='X':
                graph[i][j]='O'
                dfs(count+1)
                graph[i][j]='X'

dfs(0)    
if ans2==True:
    print("YES")
else:
    print("NO")

    



     
