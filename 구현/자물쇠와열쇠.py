import sys

input=sys.stdin.readline

#자물쇠와열쇠, 참고용

#[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def check():
    for i in range(n):
        for j in range(n):
            if lock[i][j]==0:
                return False
    return True

def right(key):
    temp=[[0]*n for _ in range(n)]
    for i in range(len(key)):
        for j in range(len(key)):
            temp[i][j]=key[i][j]
    for i in range(len(key)):
        for j in range(1,len(key)):
            key[i][j]=temp[i][j-1]
    
# 팀노트에서 활용해도좋음
def rot(n,key):
    temp=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=key[i][j]
    
    for i in range(n):
        for j in range(n):
            key[j][i]=temp[n-1-i][j]
          
    print(key)
   
