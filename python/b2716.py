N = int(input())
for _ in range(N):
    st = input()
    row = 0
    max_row = 0
    for ch in st:
        if ch == "[":
            row += 1
        else:
            max_row = max(row, max_row)
            row -= 1
  
    print(1 << max_row)