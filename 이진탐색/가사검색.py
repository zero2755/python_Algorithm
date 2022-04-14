#카카오 가사검색, 최적화 필요
from bisect import bisect_left, bisect_right

def solution(words, queries):
    
    answer = []
    Arr=[[] for _ in range(100001)]
    Arr2=[[] for _ in range(100001)]
    words.sort()
    
    for word in words:
        
        Arr[len(word)].append(word)
        Arr2[len(word)].append(word)
     
    for i in range(100001):
        if len(Arr[i])!=0:
            #print(Arr[i])
            zxc=3
        if len(Arr2[i])!=0:
            for x in Arr2[i]:
                lenX=len(x)
                tempReverseStr=""
                for y in range(lenX):
                    tempReverseStr+=x[lenX-y-1]
                #x=tempReverseStr
                #print("리버스",tempReverseStr)
                #print(x,"바뀐?")
                Arr2[i][Arr2[i].index(x)] = tempReverseStr
            #print(Arr2[i],"요건?")
        
    #print("@@@@@@@@@@@@")
    #print(queries)
    #print("@@@@@@@@@@@@")
    #print(Arr2)
    for q in queries:
        #print(q,"바뀌기전")
        tempStr1=""
        tempStr2=""
        lenQ=len(q)
        if q[0]=="?":
            tempReverseStr=""
            for i in range(lenQ):
                tempReverseStr+=q[lenQ-i-1]
            #print(tempReverseStr,"z")
            
            for i in range(lenQ):
                #print("==========================")
                #print(q)
                #0,1,2,3
                #길이가4 라면 lenQ-i-1 이면 3,2,1,0
                #print("==========================")
                if q[lenQ-i-1]=='?':
                    tempStr1+="a"
                    tempStr2+="z"
                else:
                    tempStr1+=q[lenQ-i-1]
                    tempStr2+=q[lenQ-i-1]
            
            #q="".join(tempReverseStr)
            #print(q)
            #print(tempStr1,"str1")
            #print(tempStr2,"str2")
            Arr2[lenQ].sort()
            idx1=bisect_left(Arr2[lenQ],tempStr1)
            idx2=bisect_right(Arr2[lenQ],tempStr2)
            #print(idx1,"idx1")
            #print(idx2,"idx2")
            answer.append(idx2-idx1)
        else:
            for i in range(lenQ):
                if q[i]=='?':
                    tempStr1+="a"
                    tempStr2+="z"
                else:
                    tempStr1+=q[i]
                    tempStr2+=q[i]

            idx1=bisect_left(Arr[lenQ],tempStr1)
            idx2=bisect_right(Arr[lenQ],tempStr2)
            
       
            answer.append(idx2-idx1)
            
             
    #print("정답")
    #print(answer)
    return answer
