def solution(d, budget):
    cnt=0
    d.sort()
    for x in d:
        if budget>=x:
            cnt+=1
            budget-=x
        else:
            break
    
    
    
    answer = cnt
    return answer
