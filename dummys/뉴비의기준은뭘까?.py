
#백준(BOJ) 19944
N,M=map(int,input().split())

def prt(N,M):
    if M==1 or M==2:
        return 'NEWBIE!'
    if N>=M:
        return 'OLDBIE!'
    else:
        return 'TLE!'


print(prt(N,M))
