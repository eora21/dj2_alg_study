import sys
sys.setrecursionlimit(10**9)

def squre_check(r, c):
    squre_num = min(10 - max(r, c), 5)
    for r_adder in range(5):
        if r_adder >= squre_num:
            break

        max_row_num = 0
        for c_adder in range(5):
            if c_adder >= squre_num:
                break

            if paper[r + r_adder][c + c_adder]:
                max_row_num += 1
            else:
                if r_adder >= max_row_num:
                    return r_adder
                else:
                    squre_num = min(squre_num, max_row_num)
    
    return squre_num


def DFS(ticket=0):
    global total
    if ticket >= total:
        return

    for row in range(10):
        for col in range(10):
            if paper[row][col]:
                num = squre_check(row, col)
                

                for r_to0 in range(num):
                    for c_to0 in range(num):
                        paper[row + r_to0][col + c_to0] = 0

                for repeat in range(num, -1, -1):
                    if repeat != num:
                        for r_to1 in range(repeat):
                            paper[row + r_to1][col + repeat] = 1
                        for c_to1 in range(repeat + 1):
                            paper[row + repeat][col + c_to1] = 1

                    if repeat > 0 and confetti[repeat - 1]:
                        confetti[repeat - 1] -= 1
                        DFS(ticket + 1)
                        confetti[repeat - 1] += 1

                return
    
    total = min(total, ticket)
    

paper = [list(map(int, input().split())) for _ in range(10)]
confetti = [5, 5, 5, 5, 5]
total = 26
DFS()
print("-1" if total == 26 else total)