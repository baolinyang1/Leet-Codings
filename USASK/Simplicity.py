# Count = {}
# CharSet = set()

# string = input()

# for i in string:
#     if i in CharSet:
#         Count[i] += 1
#     if i not in CharSet:
#         Count[i] = 1
#         CharSet.add(i)

# result = list(Count.values())
# result.sort()
# final = 0

# for i in range(0, len(result)-2):
#     final += 1


# print(final)

from collections import Counter

s = input().strip()
best1 = best2 = 0
for v in Counter(s).values():
    if v > best1:
        best1, best2 = v, best1
    elif v > best2:
        best2 = v
print(len(s) - best1 - best2)
