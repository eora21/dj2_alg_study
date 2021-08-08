def find_max_total(f_li, mode):
    if mode:
        for s in range(len(f_li)):
            if f_li[s] == "+":
                f_li[s] = "-"
            elif f_li[s] == "-":
                f_li[s] = "+"
    total = 0
    plus = True
    flag = True
    total_min = 0
    if len(f_li) == 1:
        return f_li[0]
    for j in range(len(f_li)):
        if type(f_li[j]) is int:
            if plus:
                total += f_li[j]
            else:
                total -= f_li[j]
        elif f_li[j] == "-":
            plus = False
            if flag:
                total_min = total - find_max_total(f_li[j+1:], True)
                flag = False
        else:
            plus = True
    return total if total < total_min else total_min


string = input()
li = []
cut = 0
for i in range(len(string)):
    if string[i] == "+" or string[i] == "-":
        li.append(int(string[cut:i]))
        li.append(string[i])
        cut = i + 1
li.append(int(string[cut:]))

print(find_max_total(li, False))