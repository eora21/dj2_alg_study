st = input()
UCPC = "UCPC"

i = 0
cnt = 0

while(cnt < 4 and i < len(st)):
    if st[i] == UCPC[cnt]:
        cnt += 1
    i += 1

if cnt >= 4:
    print("I love UCPC")
else :
    print("I hate UCPC")