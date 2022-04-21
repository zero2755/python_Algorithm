N=int(input())

inputArr=[]
for i in range(N):
    inputArr.append(int(input()))
ansArr=[[0,0] for _ in range(N)]
ansArr[0][0]=inputArr[0]
ansArr[0][1]=inputArr[0]


if N!=1:
    ansArr[1][0]=inputArr[0]+inputArr[1]
    ansArr[1][1]=inputArr[1]

if N!=1:
    for i in range(2,N):
        ansArr[i][0]=ansArr[i-1][1]+inputArr[i]
        ansArr[i][1]=max(ansArr[i-2][0],ansArr[i-2][1])+inputArr[i]



print(max(ansArr[N-1][0],ansArr[N-1][1]))
