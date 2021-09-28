def delete_sudoku(d):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] >= 10 * d:
                sudoku[i][j] = 0
    return False


def make_sudoku(d=0):
    make_min = False

    while True:
        flag = True
        not_changed = True

        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    flag = False
                    horizontal = set(sudoku[row])
                    vertical = set(sudoku[y][col] for y in range(9))
                    r = row // 3 * 3
                    c= col // 3 * 3
                    square = set(sudoku[y][x] for y in range(r, r+3) for x in range(c, c+3))
                    
                    not_possible_set = horizontal | vertical | square

                    while True:
                        repeat = False
                        for i in not_possible_set:
                            if i > 10:
                                not_possible_set.remove(i)
                                not_possible_set.add(i % 10)
                                repeat = True
                                break

                        if not repeat:
                            break
                    
                    possible_set = OtoN - not_possible_set

                    if not possible_set:
                        delete_sudoku(d)
                        return False

                    elif len(possible_set) == 1:
                        sudoku[row][col] = 10 * d + (possible_set.pop())
                        not_changed = False

                    elif make_min:
                        li = sorted(list(possible_set))
                        for num in li:
                            sudoku[row][col] = 10 * (d+1) + num
                            if make_sudoku(d+1):
                                return True
                        else:
                            delete_sudoku(d)
                            return False

        if flag:
            return True
        
        elif not_changed:
            make_min = True


OtoN = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sudoku = [list(map(int, input())) for _ in range(9)]

make_sudoku()

for i in range(9):
    for j in range(9):
        print(sudoku[i][j] % 10, end="")
    print()