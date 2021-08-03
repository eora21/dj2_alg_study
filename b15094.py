st = input()
UCPC = "UCPC"

i = 0
j = 0

while(j < 4 and i < len(st)):
    if st[i] == UCPC[j]:
        j += 1
    i += 1

if j >= 4:
    print("I love UCPC")
else :
    print("I hate UCPC")