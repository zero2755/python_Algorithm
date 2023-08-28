def solution(s):
    answer = len(s)

    sLen = len(s)
    #print(sLen)
    tempAns = ''
    for unit in range(1, sLen // 2 + 1):
        tempAns = ''
        priv = s[0:unit]

        cur = ''

        cnt = 0
        for curSor in range(unit, sLen, unit):
            cur = s[curSor:curSor + unit]
            #print(priv, cur, curSor, '흠')

            if curSor==5:
                abc=3
            elif curSor==6:
                abc=4
            elif curSor==7:
                abc=8

            if priv == cur:
                # print(priv,cur,'굳')
                cnt += 1
            else:  # pirv랑 cur다를때
                if cnt == 0:
                    tempAns += priv

                else:
                    tempAns += str(cnt + 1) + priv
                priv = s[curSor:curSor + unit]
                cnt = 0
        if cnt==0:
            tempAns += cur  # 나머지 처리
        else:
            tempAns += str(cnt + 1) + priv

        #print(tempAns)
        answer=min(answer,len(tempAns))


    return answer
