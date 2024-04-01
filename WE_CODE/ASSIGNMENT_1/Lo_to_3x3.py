# Khởi tạo ma trận rỗng
matrix = []
check_matrix = [[0,0,0], [0,0,0], [0,0,0]]

# Số hàng và số cột của ma trận
rows = 3
cols = 3

#print("Nhập ma trận:")
for i in range(rows):
    # Nhập từng dòng của ma trận
    row = list(map(int, input().split()))    
    # Thêm dòng vào ma trận
    matrix.append(row)


n = int(input())

def is_win(x, y):
    #print(x, y, '\n')
    
    #check row------------
    ok = 1
    for i in range(rows):
        if check_matrix[i][y] == 0:
            ok = 0

    if ok == 1:
        return ok
    #----------------------

    #check col-------------
    ok = 1
    for j in range(cols):
        if check_matrix[x][j] == 0:
            ok = 0
    #----------------------    

    #check cross-----------
    if check_matrix[0][0]==1 and check_matrix[1][1] == 1 and check_matrix[2][2] == 1 :
        return 1;

    if check_matrix[0][2]==1 and check_matrix[1][1] == 1 and check_matrix[2][0] == 1 :
        return 1;
    #----------------------

    return ok


won = 0

for loop in range(n):
    temp = int(input())

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == temp:
                check_matrix[i][j] = 1
                
                if is_win(i, j) == 1:
                    won = 1
                    break  # Exit the j loop
                    break  # Exit the i loop

    if won == 1:
        break  # Exit the loop



if won == 1:
    print("Yes")
else:
    print("No")

#print(check_matrix)
