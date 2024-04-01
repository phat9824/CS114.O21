# Khởi tạo ma trận rỗng
matrix = []

# Số hàng và số cột của ma trận
rows = 2
cols = 2

check = [[0, 0], [0, 0]]

# print("Nhập ma trận:")
for i in range(rows):
    # Nhập từng dòng của ma trận
    row = list(input())
    # Thêm dòng vào ma trận
    matrix.append(row)

# dem lien thong
count1 = 0


def solve(i, j):

    global count1

    if matrix[i][j] == "#" and check[i][j] == 0:
        # print (i , j,'\n')
        check[i][j] = 1
        count1 = count1 + 1

    if i+1 < rows :
        if matrix[i + 1][j] == "#" :
            solve(i + 1, j)

    if j+1 < cols:
        if matrix[i][j + 1] == "#" :
            solve(i, j + 1)


solve(0, 0)

# dem cac ky tu # co trong matran
count2 = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "#":
            count2 = count2 + 1

if count2 == 0:
    print("No")
elif count2 == 2 and check[1][0] == 1 and check[0][1] == 1:
    print("No")
else:
    if count1 == count2:
        print("Yes")
    else:
        print("No")
    
