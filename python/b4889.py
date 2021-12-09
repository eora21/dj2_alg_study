import sys
input = sys.stdin.readline

case = 1

while True:
    st = input().rstrip('\n')
    if '-' in st:
        break

    total = 0
    open_num = 0
    for ch in st:
        if ch == '{':
            open_num += 1
        else:
            if open_num > 0:
                open_num -= 1
            else:
                total += 1
                open_num += 1
    print("{}. {}".format(case, total + open_num // 2 + open_num % 2))
    case += 1