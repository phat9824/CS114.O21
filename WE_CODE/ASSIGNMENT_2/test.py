l, n = map(int, input().split())
left_queue, right_queue = [], []
l = l*100
len_left = 0
len_right = 0

for _ in range(n):
    length, position = input().split()
    length = int(length)
    if position == "left":
        left_queue.append(length)
        len_left += 1
    else:
        right_queue.append(length)
        len_right +=1

ferry_position = "left"
trips = 0

while len_left > 0  or len_right > 0:
    total_length = 0
    if ferry_position == "left":
        if len_left > 0:
            while left_queue and total_length + left_queue[0] <= l:
                
                total_length += left_queue[0]
                left_queue.pop(0)
                len_left -= 1
    else:
        if len_right > 0:
            while right_queue and total_length + right_queue[0] <= l:

                total_length += right_queue[0]
                right_queue.pop(0)
                len_right -= 1

    #print(total_length)
    trips += 1
    ferry_position = "right" if ferry_position == "left" else "left"

print(trips)

# 'https://www.youtube.com/watch?v=6hdjlWd_P9M' có tham khảo cách giải bài ferry loading IV