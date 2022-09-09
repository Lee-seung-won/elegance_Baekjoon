import sys
input = sys.stdin.readline

####10815 수정버전 ####
plus_n = [0]*(10**7) + [0]
minus_n = [0]*(10**7) + [0]

num_get = int(input())
getN = list(map(int,input().split()))
for n in getN:
    if n>=0:
        plus_n[n] += 1# 수정부분
    else:
        minus_n[-n] += 1# 수정부분
        

num_sug = int(input())
sugN = list(map(int,input().split()))

result = []
for n in sugN:
    if n>=0:
        result.append(plus_n[n])
    else:
        result.append(minus_n[-n])

#출력
for n in result:
    print(n, end=' ')

