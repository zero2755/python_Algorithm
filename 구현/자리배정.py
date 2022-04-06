from collections import deque
from itertools import permutations
from itertools import combinations
import sys
import heapq

input=sys.stdin.readline

#더미, 구현, 비슷한유형 정리필요
#https://www.acmicpc.net/problem/10157

M,N=map(int,input().split())

K=int(input())
INF=987654321
graph=[[INF]*M for _ in range(N)]
#N-1,0에서시작 방향을 상우하좌로
dx=[-1,0,1,0]
dy=[0,1,0,-1]
#print(graph)
i=0
curNum=1
#처음한바ㅜ키는 상하좌우 인덱스조건필요, 그다음에는 987654321인지아닌지만확인 
toggle1=True
toggle2=True
toggle3=True
toggle4=True
curX=N-1
curY=0

myToggle=0
if K>N*M:
    print(0)
    myToggle=1

while myToggle==0:
    
    graph[curX][curY]=curNum
    if curNum==K:
        print(curY+1,N-curX)
        break
    curNum+=1
    
    if curX-1<0 and toggle1==True:
        i=(i+1)%4
        toggle1=False
        #print("1")
    if curY+1==M and toggle2==True:
        i=(i+1)%4
        toggle2=False
        #print("2")
    if curX+1==N and toggle3==True and toggle1==False:
        i=(i+1)%4
        toggle3=False
        #print("3")
    
    toggle4=False
         
    curX,curY=curX+dx[i],curY+dy[i]
    if curNum>N*M:
        break
    if graph[curX][curY]!=INF and toggle1==False and toggle2==False and toggle3==False and toggle4==False:
        curX,curY=curX-dx[i],curY-dy[i]
        i=(i+1)%4
        curX,curY=curX+dx[i],curY+dy[i]
         
    elif toggle4==False and toggle1==False and toggle2==False and toggle3==False and graph[curX][curY]!=INF:
         
        break
#print(graph)



