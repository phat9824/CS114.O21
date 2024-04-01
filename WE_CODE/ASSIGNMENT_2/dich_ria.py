import sys

r, c = list(map(int, sys.stdin.readline().strip().split()))
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(r)]


k = 0
chk = []
# khoi tao toan bo bien check  = 0
for i in range(r):
    t = []
    for j in range(c):
        t.append(0)
    chk.append(t)


def print_arr(arr):

    for x in range(r):
        for y in range(c-1):
            print(arr[x][y], end=" ")
        print(arr[x][c - 1])


def rotate_clockwise(arr, chk, k):
    temp = arr[k][k]

    # chk[k][k] = 1
    # duyet dong ngang tren
    for j in range(k + 1, c - k):
        sub_temp = arr[k][j]
        arr[k][j] = temp
        chk[k][j] = 1
        temp = sub_temp

    # duyet cot ben phai
    # print(arr[k][c - k - 1])
    for j in range(k + 1, r - k):
        sub_temp = arr[j][c - k - 1]
        arr[j][c - k - 1] = temp
        chk[j][c - k - 1] = 1
        temp = sub_temp

    # print(arr[r - k - 1][c - k - 1])
    # duyet dong ngang duoi
    for j in range((c - k - 1) - 1, k - 1, -1):
        sub_temp = arr[r - k - 1][j]
        if chk[r - k - 1][j] == 0:
            arr[r - k - 1][j] = temp
            chk[r - k - 1][j] = 1
            temp = sub_temp

    # duyet cot ben trai
    # print(arr[r - k -1][k])
    for j in range((r - k - 1) - 1, k - 1, -1):
        sub_temp = arr[j][k]
        if chk[j][k] == 0:
            arr[j][k] = temp
            chk[j][k] = 1
            temp = sub_temp

    return arr, chk


def rotate_not_clockwise(arr, chk, k):
    temp = arr[r - k - 1][c - k - 1]

    # duyet cot ben phai
    for j in range((r - k - 1) - 1, k - 1, -1):
        sub_temp = arr[j][c - k - 1]
        arr[j][c - k - 1] = temp
        chk[j][c - k - 1] = 1
        temp = sub_temp

    # duyet dong ngang tren
    for j in range( (c - k - 1) - 1 , k - 1 , -1):
        sub_temp = arr[k][j]
        
        arr[k][j] = temp
        chk[k][j] = 1
        temp = sub_temp

    # duyet cot ben trai
    for j in range(k + 1, r - k):
        
        sub_temp = arr[j][k]
        if chk[j][k] == 0:
            arr[j][k] = temp
            chk[j][k] = 1
            temp = sub_temp
    
    # duyet dong ngang duoi
    for j in range(k + 1, (c - k)):
        # print(arr[r - k  - 1][j])
        sub_temp = arr[r - k - 1][j]
        if chk[r - k - 1][j] == 0:
            arr[r - k - 1][j] = temp
            chk[r - k - 1][j] = 1
            temp = sub_temp
        
    return arr, chk


limit = int(min(r, c))
for k in range(limit):
    if chk[k][k] == 1:
        break
    # vi tri vong ma tran
    if (k) % 2 == 0:
        arr, chk = rotate_clockwise(arr, chk, k)
    else:
        arr, chk = rotate_not_clockwise(arr, chk, k)

        # print(chk)

print_arr(arr)
