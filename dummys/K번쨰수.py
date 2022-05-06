def solution(array, commands):
    answer = []
    arLen=len(commands)
    #print("============")
    for i in range(arLen):
        
        arr = array[commands[i][0]-1:commands[i][1]]
        
        arr.sort()
        
        answer.append(arr[commands[i][2]-1])
    
    return answer
  
  #https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
