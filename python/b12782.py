for _ in range(int(input())):
    N, M = input().split()

    diff_cnt = [0, 0]

    for i in range(len(N)):
        if N[i] != M[i]:
            diff_cnt[int(M[i])] += 1
    
    print(max(diff_cnt))