import sys
input = sys.stdin.readline

## 첫번째 방법 - ![시간초과]!
###가지고 있는 숫자카드 입력
##num_get = int(input())
##getN = list(map(int,input().split()))
##    
###제시된 숫자카드 입력
##num_sug = int(input())
##sugN = list(map(int,input().split()))
##
##result = []
##for n in sugN:
##    if n in getN:
##        result.append(1)
##    else:
##        result.append(0)
##
###출력
##for n in result:
##    print(n, end=' ')

#두번째 방법
plus_n = [0]*(10**7) + [0]
minus_n = [0]*(10**7) + [0]

num_get = int(input())
getN = list(map(int,input().split()))
for n in getN:
    if n>=0:
        plus_n[n] = 1
    else:
        minus_n[-n] = 1
        

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



            



