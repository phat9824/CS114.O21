def phan_tich_thua_so_nguyen_to(n):
    # khoi tao mot chua cac thua so nguyen to va so mu cua no
    arr = []
    # kiem tra cac so nguyen tu 2 -> sqrt n
    k = 2
    dem = 0
    while n % k == 0:
            #Neu co tuc la co binh phuong cua 1 so n co the chia duoc nen k chay nua
            # neu khong thi n chia i
            if dem > 0:
                return arr, 0
            else:
                arr.append(k)
                dem+=1
            n = int(n / k)

    k = 3
    while k * k <= n:
        # kiem tra n co phai thua so cua i
        dem = 0
        while n % k == 0:
            #Neu co tuc la co binh phuong cua 1 so n co the chia duoc nen k chay nua
            # neu khong thi n chia i
            if dem > 0:
                return arr, 0
            else:
                arr.append(k)
                dem+=1
            n = int(n / k)
        k += 2

    # CASE n van con va n < k
    if n > 1:
        arr.append(n)

    return arr, 1

def dem_so_cap(L, R):

    count = 0

    tap_thua_so_da_pt = []
    so_dac_biet = []
    
    res = []
    chk = 0

    for k in range(L, R+1):
        res , chk = phan_tich_thua_so_nguyen_to(k)
        if chk == 1:
            so_dac_biet.append(k)
            tap_thua_so_da_pt.append(res)

    #print(so_dac_biet)
    len_so_dacbiet = len(so_dac_biet)
    #print(len_so_dacbiet)
    for i in range(len_so_dacbiet-1):

        for j in range(i+1, len_so_dacbiet):
            
            tmp_chk = 1
            
            if len(tap_thua_so_da_pt[i]) < len(tap_thua_so_da_pt[j]):
                for key in tap_thua_so_da_pt[i]:
                    if so_dac_biet[j] % key == 0:
                        tmp_chk = 0
                        break
            else: 
                for key in tap_thua_so_da_pt[j]:
                    if so_dac_biet[i] % key == 0:
                        tmp_chk = 0
                        break
                
            if tmp_chk == 1:
                count+=1
                #print(so_dac_biet[i],so_dac_biet[j])

    
    return count


import sys

# Input
LR = tuple(map(int, sys.stdin.readline().strip().split()))
# Output
result = dem_so_cap(LR[0], LR[1])
print(result)



