string = input()
li = []
cut = 0
for i in range(len(string)):
    if string[i] == "+" or string[i] == "-":
        li.append(int(string[cut:i]))
        li.append(string[i])
        cut = i + 1
li.append(int(string[cut:]))

total = 0
mode = True
for j in range(len(li)):
    if type(li[j]) is int:
        if mode:
            total += li[j]
        else:
            total -= li[j]
            
    elif mode and li[j] == "-":
        mode = False

print(total)