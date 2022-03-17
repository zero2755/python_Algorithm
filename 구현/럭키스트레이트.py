

#백준 18406번
 

str=input()

strLen=len(str)

strLenHalf=len(str)//2
 
sum1=0
for i in range(0,strLenHalf):
    sum1+=int(str[i])
     

sum2=0
for i in range(strLenHalf,strLen):
    sum2+=int(str[i])
     

if(sum1==sum2):
    print("LUCKY")
else:
    print("READY") 
