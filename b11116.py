N = int(input())
for n in range(N):
    m = int(input()) 
    left = sorted(list(map(int, input().split())))
    right = sorted(list(map(int, input().split())))
    cnt = 0
    i = 0
    while True:
        try:
            w = left[i]
            if w + 500 in left and w + 1000 in right and w + 1500 in right:
                cnt += 1
                del(left[i])
                left.remove(w + 500)
                right.remove(w + 1000)
                right.remove(w + 1500)
            else:
                i += 1
        except IndexError:
            break
    
    print(cnt)
