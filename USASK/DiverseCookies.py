# Read number of people N (not used) and counts of the three cookie types
N, A, B, C = map(int, input().split())

# Total number of cookies baked
total = A + B + C

# Number of cookies that are NOT the most frequent type
# (used to separate the dominant cookie type)
other = total - max(A, B, C)

# Maximum cookies that can be eaten without two identical cookies in a row:
# either all cookies, or limited by how many separators exist
print(min(total, 2 * other + N))
