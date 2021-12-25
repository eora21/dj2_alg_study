N = int(input())
alps = {}
strs = [list(input()) for _ in range(N)]
for st in strs:
    l = len(st)
    for col in range(l):
        try:
            alps[st[col]] += 10 ** (l - col - 1)
        except:
            alps[st[col]] = 10 ** (l - col - 1)

sort_alps = sorted(alps.items(), key=lambda x: x[1], reverse=True)

new_dicts = {}
new_val = 9
for ch, _ in sort_alps:
    new_dicts[ch] = new_val
    new_val -= 1

for row in range(N):
    for col in range(len(strs[row])):
        strs[row][col] = new_dicts[strs[row][col]]

total = 0
for row in range(N):
    l = len(strs[row])
    t = 1
    for col in range(l-1, -1, -1):
        total += t * strs[row][col]
        t *= 10

print(total)