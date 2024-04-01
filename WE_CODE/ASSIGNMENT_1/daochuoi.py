n = int(input())
for k in range(n):

    a = input()
    b = input()

    if a != "" and b != "":
        x_A = ""  # Chuỗi x để lưu trữ các ký tự lẻ
        y_A = ""  # Chuỗi y để lưu trữ các ký tự chẵn

        x_B = ""  # Chuỗi x để lưu trữ các ký tự lẻ
        y_B = ""  # Chuỗi y để lưu trữ các ký tự chẵn

        for i in range(len(a)):
            if i % 2 == 0:
                x_A += a[i]
            else:
                y_A += a[i]

            
        for i in range(len(b)):
            if i % 2 == 0:
                x_B += b[i]
            else:
                y_B += b[i]
        


        # Sắp xếp các chuỗi
        if x_A != "":
            x_A = sorted(x_A)
        if x_B != "":
            x_B = sorted(x_B)
        if y_A != "":
            y_A = sorted(y_A)
        if y_B != "":
            y_B = sorted(y_B)

        if x_A == x_B and y_A == y_B:
            print("YES\n")
        else:
            print("NO\n")
    elif a == "" and b != "":
        print("NO\n")
    elif a != "" and b == "":
        print("NO\n")
    else:
        print("YES\n")
