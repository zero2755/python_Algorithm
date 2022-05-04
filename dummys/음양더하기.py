def solution(absolutes, signs):
    
    tempAns=0
    
    tempLen=len(signs)
    #
    for i in range(tempLen):
        print(signs[i])
        if signs[i]==True:
            tempAns+=absolutes[i]
        else:
            tempAns-=absolutes[i]
    
    
    answer=tempAns
    
    return answer
