import math

n = int(input())
count = 0
square_n = n*n
limit = int( n/ math.sqrt(2) ) - 1
for i in range( 1, limit ):
    tmp = square_n - i * i
    if math.sqrt(tmp).is_integer():
        count += 1
print(count)