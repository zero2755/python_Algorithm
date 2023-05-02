#10분
N= int(input())

arr=list(map(int,input().split()))

#print(arr)



def search(start,end):

    if start>end:
        return -1
    mid=(start+end)//2

    if mid==arr[mid]:
        return mid
    elif arr[mid]>mid:
        return search(start,mid-1)
    elif arr[mid]<mid:
        return search(mid+1,end)


result=search(0,len(arr)-1)

print(result)
