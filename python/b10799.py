st = input()
total = 0
num = 0
before = ""
for now in st:
    if now == ")":
        num -= 1
        total += num if before == "(" else 1
    else:
        num += 1
    
    before = now

print(total)
