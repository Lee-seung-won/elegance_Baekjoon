import sys
input = sys.stdin.readline

S = input().strip()
num = 0
sep_string = []
for i in range(1, len(S)+1):
    for j in range(len(S)-(i-1)):
        sep_string.append(S[j:j+i])

print(len(set(sep_string)))


        
