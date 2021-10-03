N = int(input())

dic = {}
for _ in range(N):
    L, H = map(int, input().split())
    dic[L] = H

dic_key_sort = sorted(dic.keys())
dic_values_sort = [dic[key] for key in dic_key_sort]

col = 0
height = 0
total = 0

for i in range(len(dic_key_sort)):
    now_col = dic_key_sort[i]
    now_height = dic_values_sort[i]

    try:
        next_max_height = max(dic_values_sort[i+1:])
    except ValueError:
        next_max_height = 0
    
    total += height * (now_col - col)

    if height <= now_height <= next_max_height:
        height = now_height
    elif now_height > next_max_height:
        total += now_height - next_max_height
        height = next_max_height

    col = now_col
    
print(total)