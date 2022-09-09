import sys
input = sys.stdin.readline

######첫번째방법 - !시간초과!
##n,m = map(int,input().split())
##no_listen = []
##for _ in range(n):
##    name = input().strip()
##    no_listen.append(name)
##
##no_see = []
##for _ in range(m):
##    name = input().strip()
##    no_see.append(name)
##no_see_listen=[]
##for p in no_see:
##    if p in no_listen:
##        no_see_listen.append(p)
##
##no_see_listen.sort()
##print(len(no_see_listen))
##for p in no_see_listen:
##    print(p)

#####두번째방법 - 시간초과
##n,m = map(int,input().split())
##no_listen = {}
##for _ in range(n):
##    name = input().strip()
##    if name[0] not in no_listen.keys():
##        no_listen[name[0]] = []
##    no_listen[name[0]].append(name)
##
##no_see_listen=[]
##for _ in range(m):
##    name = input().strip()
##    if name in no_listen[name[0]]:
##        no_see_listen.append(name)
##
##no_see_listen.sort()
##print(len(no_see_listen))
##for p in no_see_listen:
##    print(p)


#####세번째방법 - 집합사용 (속도 완전 빠름)
n,m = map(int,input().split())
no_listen = []
for _ in range(n):
    name = input().strip()
    no_listen.append(name)
no_listen = set(no_listen)

no_see = []
for _ in range(m):
    name = input().strip()
    no_see.append(name)
no_see = set(no_see)

no_see_listen = list(no_see & no_listen)

no_see_listen.sort()
print(len(no_see_listen))
for p in no_see_listen:
    print(p)
