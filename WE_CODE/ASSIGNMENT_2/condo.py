l, m = map(int, input().split())
left_queue, right_queue = [], []
len_left = 0
len_right = 0

for _ in range(m):
    length, position = input().split()
    length = int(length)
    if position == "left":
        left_queue.append(length)
        len_left += 1
    else:
        right_queue.append(length)
        len_right += 1

ferry_position = "left"
trips = 0

while len_left > 0 or len_right > 0:
    total_length = 0

    if ferry_position == "left" and left_queue and total_length + left_queue[0] <= l:
        while left_queue and total_length + left_queue[0] <= l:
            total_length += left_queue[0]
            left_queue.pop(0)
            len_left -= 1
    elif ferry_position == "right" and right_queue and total_length + right_queue[0] <= l:
        while right_queue and total_length + right_queue[0] <= l:
            total_length += right_queue[0]
            right_queue.pop(0)
            len_right -= 1

    trips += 1
    ferry_position = "right" if ferry_position == "left" else "left"

print(trips)
