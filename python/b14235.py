import sys, heapq
input = sys.stdin.readline

gift = []

n = int(input())
for _ in range(n):
    st = list(map(int, input().split()))
    if st[0]:
        for i in st[1:]:
            heapq.heappush(gift, -i)
    else:
        print(-heapq.heappop(gift) if gift else "-1")