import sys
input = sys.stdin.readline

n,m = map(int,input().split())
#포켓몬 도감 등록하기
monster_dic = {} # 딕셔너리 {이름:번호} 형태
monster_list = [0] # 리스트 [(인덱스)이름] 형태
for i in range(1, n+1):
    name = input().strip()
    monster_dic[name] = i
    monster_list.append(name)

#단어 제시 받기
sug_list = []
for _ in range(m):
    temp = input()
    try:
        ip = int(temp)
    except:
        ip = temp.strip()
    sug_list.append(ip)

#제시받은 단어 도감에서 찾아 출력하기
for s in sug_list:
    if type(s) == int:
        print(monster_list[s])
    else:
        print(monster_dic[s])
