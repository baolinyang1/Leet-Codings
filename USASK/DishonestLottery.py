# n = int(input())
# nums = []
# for i in range(0, 10 * n):
#     arr = [int(i) for i in input().split()]
#     nums.extend(arr)

# threshold = 2 * n
# nums.sort()
# counter = 0
# dis = nums[0]
# result = []
# for i in nums:
#     if i == dis:
#         counter += 1
#         if counter > threshold:
#             result.append(i)
#     else:
#         dis = i
#         counter = 1

# print(' '.join(map(str, result)))
    

    


n = int(input())

# Count appearances of numbers 1..50
count = [0] * 51  # index 0 unused

# There are 10 * n drawings
for _ in range(10 * n):
    nums = map(int, input().split())
    for x in nums:
        count[x] += 1

# Find suspicious numbers
suspicious = []
for num in range(1, 51):
    if count[num] > 2 * n:
        suspicious.append(num)

# Output result
if suspicious:
    print(" ".join(map(str, suspicious)))
else:
    print(-1)

