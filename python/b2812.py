N, K = map(int, input().split())
st = list(input())

front = 0
tail = 1
while K:
    while not st[front]:
        front += 1

    tail = front + 1
    try:
        while not st[tail]:
            tail += 1
    except:
        st[front] = ''
        front = 0
        tail = 1
        K -= 1
        continue

    if st[front] < st[tail]:
        st[front] = ''
        K -= 1
        
        while not st[front] and front:
            front -= 1
            
    else:
        front += 1
        front %= N

print(''.join(st))