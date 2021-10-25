def check(st):
    twins = {")": "(", "]": "["}
    num = {")": 2, "]": 3}
    stack = []

    try:
        for ch in st:
            if ch == "(" or ch == "[":
                stack.append(ch)
            else:
                if stack[-1] == twins[ch]:
                    stack.pop()
                    stack.append(num[ch])
                else:
                    for i in range(len(stack) - 1, -1, -1):
                        if not (type(stack[i]) is int) and stack[i] != twins[ch]:
                            return 0
                        elif stack[i] == twins[ch]:
                            stack.append(sum(stack[i + 1:] * num[ch]))
                            del(stack[i:-1])
                            break
                    else:
                        return 0
                        
        return sum(stack)
    except:
        return 0

print(check(input()))