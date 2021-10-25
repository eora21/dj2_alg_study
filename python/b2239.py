def make_sudoku():
    nums = [True] * 10
    nums[0] = False
    
    for row in range(0, 9):
        for col in range(0, 9):
            if sudoku[row][col] == 0:
                horizontal = sudoku[row]
                for i in horizontal:
                    nums[i] = False

                vertical = [sudoku[y][col] for y in range(9)]
                for j in vertical:
                    nums[j] = False

                r = row // 3 * 3
                c= col // 3 * 3
                square = [sudoku[y][x] for y in range(r, r+3) for x in range(c, c+3)]
                for k in square:
                    nums[k] = False

                for check in range(1, 10):
                    if nums[check]:
                        sudoku[row][col] = check
                        if make_sudoku():
                            return True
                        sudoku[row][col] = 0
                
                if sudoku[row][col] == 0:
                    return False

    return True

sudoku = [list(map(int, input())) for _ in range(9)]

make_sudoku()

for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end="")
    print()