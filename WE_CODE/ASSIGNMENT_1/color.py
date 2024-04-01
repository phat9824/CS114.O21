H, K, W = map(int, input().split())

# Khởi tạo mảng 2 chiều
two_dimensional_array = []

# Nhập từng phần tử của mảng
for i in range(H):
    row = input()

    # Chuyển chuỗi thành list ký tự và thêm vào mảng 2 chiều
    row_list = []
    for j in range(K):

        temp = 0

        if  row[j] == '#':
            temp = 1

        row_list.append(temp)
    # Thêm list vào mảng 2 chiều
    two_dimensional_array.append(row_list)

""" # In mảng 2 chiều
print("Mảng 2 chiều đã nhập:")
for row in two_dimensional_array:
    print(row) """

#chuyển đổi hệ thập phân sang nhị phân, "chatgpt help"
def decimal_to_binary(decimal_number, length):
    binary_representation = bin(decimal_number)[2:]
    return [0] * (length - len(binary_representation)) + [int(bit) for bit in binary_representation]

rows = [0] * H #mang chua gia tri nhi phan cho hang
cols = [0] * K #mang chua gia tri nhi phan cho cot

#print(rows, cols,'\n')

count_ans = 0

#vi moi hang co H don vi nen co 2^H cach chon to mau cho hang
#vi moi cot co K don vi nen co 2^K cach chon to mau cho cot

for i in range(2 ** H):
    
    
    temp = decimal_to_binary(i, H)#doi gia tri lan chon hang thu i ra nhi phan

    #gan gia tri cho array nhi phan cua hang
    for i1 in range(H):
        rows[i1] = temp[i1]
    #print(rows,':')
    

    for j in range(2 ** K):

        temp = decimal_to_binary(j,K)#doi gia tri lan chon cot thu i ra nhi phan
        
        #gan gia tri cho array nhi phan cua cot
        for j1 in range(K):
            cols[j1] = temp[j1]
        #print(cols)
        
        sum = 0
        for row_arr in range(H):
            if rows[row_arr] == 0: # = 0 thi khong xoa hang do, = 1 thi xoa hang do
                for col_arr in range(K):
                    if cols[col_arr] == 0: # # = 0 thi khong xoa cot do, = 1 thi xoa cot do
                        sum = sum + two_dimensional_array[row_arr][col_arr]
        
        #print(sum)

        # truong hop to mau nay dung nen chon
        if sum == W:
            count_ans = count_ans + 1


print(count_ans)


