import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 단어의 첫글자에 따라 단어 분류하기
S = {}
for _ in range(n):
    s = input().strip()
    if s[0] not in S.keys(): # S 딕셔너리에 단어 첫번째 글자가 없다면 추가하기
        S[s[0]] = []
    S[s[0]].append(s)

result = 0
for _ in range(m):
    s = input().strip()
    if s[0] not in S.keys():
        continue
    if s in S[s[0]]:
        result += 1

print(result)



