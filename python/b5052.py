def check():
    for nums in nums_list:
        node = tree
        for num in nums:
            try:
                if not node[num]:
                    return False
            except:
                node[num] = {}
            node = node[num]
    return True


for case in range(int(input())):
    n = int(input())
    nums_list = [input() for _ in range(n)]
    nums_list.sort(key=lambda x: len(x))
    tree = {}

    print("YES" if check() else "NO")
