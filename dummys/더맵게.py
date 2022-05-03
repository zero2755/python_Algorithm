from collections import deque

def solution(scoville, K):
    isFail=False
    scoville.sort()
    myQ=deque(scoville)
    tempAns=0
    if myQ[0]>K:
        return 0
    if len(myQ)==1 and myQ[0]<K:
        return -1
    while len(myQ)!=1:
        #print(myQ,"??")
        if myQ[0]<K:
            tempAns+=1
            a=myQ.popleft()
            b=myQ.popleft()
            newOne=a+b*2
            #print(a,b,newOne,"zz")
            myQ.appendleft(newOne)
            #print(myQ)
             
            scoville=list(myQ)
            scoville.sort()
            myQ=deque(scoville)
                
            #print(myQ,"zzzx")
        else:
            #print("xxc",tempAns)
            return tempAns
        if len(myQ)==1 and myQ[0]<K:
            isFail==True
    
    ans=tempAns
    if isFail==True:
        return -1
    else:
        
        return ans
