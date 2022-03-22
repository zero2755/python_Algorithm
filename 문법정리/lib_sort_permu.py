#1. 라이브러리임포트
#데큐, 이터툴

#2. 정렬 첫번째꺼 오름차순 두번째꺼 역순으로

#3. 순열, 조합, 중복조합 


#-*-coding:utf-8-*-
encoding='ISO-8859-1' 

from collections import deque

from itertools import permutations

from itertools import combinations

myList=[('A',3),('C',4),('B',1),('A',2)]


print("---------------------------------")
print(myList)
print("---------------------------------")

myList=sorted(myList, key=lambda x:(x[0], -x[1]))
print("---------첫번째오름차순 두번째 내림차순----------------")
print(myList)
print("---------------------------------")



iterToolList=[1,2,3]

iterToolList=list(permutations(iterToolList,2))
print("----------퍼뮤테이션-------------")
print(iterToolList)
print("---------------------------------")

combi=[1,2,3]
combi=list(combinations(combi,2))
print("----------콤비네이션--------------")
print(combi)
print("---------------------------------")
 
