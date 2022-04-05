#시간초과
#부루트포스
#https://www.acmicpc.net/problem/14225
N=int(input())



input_List=list(map(int,input().split()))    #입력받는 리스트
out_sum=[] #빈리스트


def go(index,tempSum):
    abc=1
    if tempSum in out_sum:
        abc=2
    #else:
    #    out_sum.append(tempSum)
    
    if(tempSum!=0 and abc==1):
        out_sum.append(tempSum)
       

    if index==N:
        return;
    tempSum+=input_List[index]
    go(index+1,tempSum)
    tempSum-=input_List[index]
    go(index+1,tempSum)








go(0,0)

for i in range(1,2000000):
     if i in out_sum:
        abc=2
     else:
        print(i)
        break





