import sys
matrix = []

r, c = map(int, sys.stdin.readline().strip().split())

max_lengths = [0] * c  # Initialize max_lengths with zeros

# Read the matrix using list comprehension
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(r)]

# Update max_lengths while reading input
for i in range(r):
        max_lengths = [max(max_lengths[j], len(str(matrix[i][j]))) for j in range(c)]

for row in matrix:
    sys.stdout.writelines( " ".join([f"{row[j]:>{max_lengths[j]}}" for j in range(len(row))]) ) 
    sys.stdout.write("\n")