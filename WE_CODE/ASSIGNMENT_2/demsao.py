import sys

matrix = []
chk = []
rows = 0
cols = 0

def make_true(r, c):
    if r - 1 >= 0:
        if matrix[r - 1][c] == "-" and chk[r - 1][c] == 0:
            chk[r - 1][c] = 1
            make_true(r - 1, c)

    if c - 1 >= 0:
        if matrix[r][c - 1] == "-" and chk[r][c - 1] == 0:
            chk[r][c - 1] = 1
            make_true(r, c - 1)

    if r + 1 < rows:
        if matrix[r + 1][c] == "-" and chk[r + 1][c] == 0:
            chk[r + 1][c] = 1
            make_true(r + 1, c)

    if c + 1 < cols:
        if matrix[r][c + 1] == "-" and chk[r][c + 1] == 0:
            chk[r][c + 1] = 1
            make_true(r, c + 1)

def solve(a, b, matrix):
    global rows, cols
    count = 0
    for i in range(a):
        for j in range(b):
            if matrix[i][j] == "-" and chk[i][j] == 0:
                count += 1
                make_true(i, j)

    return count

cnt = 1
n = int(input())
while n > 0:

    line = input().strip()

    rows, cols = list(map(int, line.split()))

    matrix = []
    chk = []

    for i in range(rows):
        row = input().strip()
        temp = [0] * cols
        chk.append(temp)
        matrix.append(row)

    # Process the test case and print the result
    result = solve(rows, cols, matrix)
    print(f'Case {cnt}: {result}')
    cnt += 1
    if cnt == 3:
        break
    n -= 1
    