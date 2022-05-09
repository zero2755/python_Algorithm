from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

curX1=1,curY1=1
curX2=2,curY2=1

def move4way():
    for i in range(4):
        nx1=curX1+dx[i]
        nx2=curX2+dx[i]
        ny1=curY1+dy[i]
        ny2=curY2+dy[i]
        if nx1>=0 and nx1<N and ny1>=0 and ny1<N and nx2>=0 and nx2<N and ny2>=0 and ny2<N:
            if graph[nx1][ny1]!=1 and graph[nx2][ny2]!=1:
                graph[nx1][ny1]=2
                graph[nx2][ny2]=2
                curX1=nx1
                curX2=nx2
                curY1=ny1
                curY2=ny2
                print("z")

#=>해당 함수는 x1,y1과 x2,y2의 상대적인 위치에따라 다를수있어 틀린함수임             
def rot1():
    #x1,y1기준축으로 x2,y2시계
    nx2=curX2+1
    ny2=curY2-1
    if nx2>=0 and nx2<N and ny2>=0 and ny2<N:
        if graph[nx2][ny2]!=1 and graph[nx2][ny2+1]!=1:
            graph[nx2][ny2]=2
            curX2=nx2
            curY2=ny2
            
        print("z")
    
    #반시계
    nx2=curX2-1
    ny2=curY2-1
    if nx2>=0 and nx2<N and ny2>=0 and ny2<N:
        if graph[nx2][ny2]!=1 and graph[nx2][ny2+1]!=1:
            graph[nx2][ny2]=2
            curX2=nx2
            curY2=ny2

def rot2():
    
    nx1=curX1+1
    ny1=curY1-1
    if nx1>=0 and nx1<N and ny1>=0 and ny1<N:
        if graph[nx1][ny1]!=1 and graph[nx1][ny1+1]!=1:
            graph[nx1][ny1]=2
            curX1=nx1
            curY1=ny1
            
        print("z")
    
    #반시계
    nx2=curX2-1
    ny2=curY2-1
    if nx2>=0 and nx2<N and ny2>=0 and ny2<N:
        if graph[nx2][ny2]!=1 and graph[nx2][ny2+1]!=1:
            graph[nx2][ny2]=2
            curX2=nx2
            curY2=ny2

def solution(board):
    answer = 0
    return answer
