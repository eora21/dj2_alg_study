T = int(input())

dic = {}

for case in range(T):
    StartTime, EndTime = map(int, input().split())
    try:
        dic[EndTime - StartTime].append(StartTime)
    except:
        dic[EndTime - StartTime] = [StartTime]

sort_li = sorted(dic.items(), key= lambda item: item[0])

print(sort_li)

"""
나중에 풀어볼 것, 개어려움
1~8, 7~9, 8~112
7~9를 선택하는 것보다 나머지 2개를 선택하는게 더 좋음
야.. 이걸 어케 생각한담?
"""