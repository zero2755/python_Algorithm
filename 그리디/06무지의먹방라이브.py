#효율성 생각할필요있음
#히든케이스찾기

def solution(food_times, k):
    
    checkSum=0
    for x in food_times:
        checkSum+=x

    if checkSum<=k:
        return -1

    answer = 0
    tgl=0
    while True:
        for i in range(len(food_times)):
            if k==0:
                answer=i+1
                
                tgl=1
                break

            if food_times[i]==0:
                continue
            else:
                food_times[i]-=1
                k-=1
        if tgl==1:
            break
        
     
    return answer
