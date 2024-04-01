

#tìm vector của 2 điểm
def calculate_vector(A, B):
    return B[0] - A[0], B[1] - A[1]

def find_square_points(A, B):
    # Tìm vectơ AB
    AB = calculate_vector(A, B)

    # Tìm vectơ vuông góc theo chiều kim đồng hồ
    perpendicular_vector = (AB[1], -AB[0])

    # Tìm các điểm C, D, C', D'
    C = (A[0] + perpendicular_vector[0], A[1] + perpendicular_vector[1])
    D = (B[0] + perpendicular_vector[0], B[1] + perpendicular_vector[1])
    
    C_prime = (A[0] - perpendicular_vector[0], A[1] - perpendicular_vector[1])
    D_prime = (B[0] - perpendicular_vector[0], B[1] - perpendicular_vector[1])
    

    return C, D, C_prime, D_prime

# Nhập tọa độ của điểm A và B
x_value, y_value = map(int, input().split())
A = (x_value, y_value)

x_value, y_value = map(int, input().split())
B = (x_value, y_value)


#tim cac diem cua tam giac
C, D, C_prime, D_prime = find_square_points(A, B)

#print(C, D , C_prime, D_prime)


def compare_points(point1, point2):
    # So sánh theo trục x
    if point1[0] < point2[0]:
        return -1  # point1 lệch về trái so với point2
    elif point1[0] > point2[0]:
        return 1   # point1 lệch về phải so với point2a
    
    # Nếu cả hai điểm có cùng hoành độ, so sánh theo tung độ
    if point1[1] < point2[1]:
        return -1  # point1 ở dưới so với point2
    elif point1[1] > point2[1]:
        return 1   # point1 ở trên so với point2
    
    return 0  # Cả hai điểm trùng nhau




if compare_points(A, B) == -1:
        print(A, C_prime, D_prime, B)
        print(A, B, D, C)

        
else:
        print(A, B, D, C)
        print(A, C_prime, D_prime, B)
        
    