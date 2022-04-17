#잘못짠코드

def solution(s):
    myLen=len(s)
    #print(s,myLen)
    #aabbaccc

    for i in range(2,myLen//2+1): #2배압축,3배압축... myLen/2배압축
        prev = s[0]
        curCnt=1
        ansStr=""+prev
        for j in range(1,myLen):
            if j==2:
                print("z")
            if prev==s[j]:
                curCnt+=1
                if curCnt==i:
                    ansStr=ansStr[:-curCnt+1]
                    ansStr+=str(i)+s[j]
                    curCnt=0
                else:
                    ansStr+=s[j]
            else:
                ansStr+=s[j]
                prev=s[j]
            print(ansStr)


            prev=s[i]
        print(ansStr,i)




    answer = 0
    return answer

solution("aabbaccc")
