import sys

def string_to_dict(input_string):
    numbers = input_string.split()
    positions_dict = {}

    for i in range(len(numbers)):
        number = numbers[i]
        if number not in positions_dict:
            positions_dict[number] = i

    return positions_dict

n = int(input())  # Read an integer from standard input
arr_string = input()  # Read a line of integers from standard input

result_dict = string_to_dict(arr_string)

m = int(input())  # Read an integer from standard input

# Read multiple lines of input for arr2
arr_string = []
arr_string = sys.stdin.readline()
arr_string = arr_string.strip().split()
for number in arr_string:
    print(result_dict.get(number, -1))
    
