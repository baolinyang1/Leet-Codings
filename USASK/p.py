# import numpy as np
# FirstLine = input()
# SecondLine = input()
# ThirdLine = input()
# FourthLine = input()

# Array_Plots = np.sort(np.fromstring(SecondLine, sep=" ", dtype=np.int64))
# Round_Houses = np.fromstring(ThirdLine, sep = " ", dtype=np.float64)
# Square_Houses = np.fromstring(FourthLine, sep=" ", dtype=np.float64)

# root2 = np.sqrt(2.0)

# results = np.sort(np.concatenate([Round_Houses, Square_Houses / root2]))

# i = 0
# j = 0
# count = 0
# eps = 1e-12

# while i < Array_Plots.size and j < results.size:
#     if Array_Plots[i] > results[j] + eps:
#         count += 1
#         j += 1
#         i += 1
#     else:
#         i += 1
# print(count)

l = [1,3,4,5]

# for i, element in enumerate(l):
#     print(i, element)


# in dict:
# each key is definitely unique, but values may not!

#case 1: u know the value and want to retrive key:
# keys = [k for k,v in dict.items() if v == '']

# m, p, n = map(int, input().split())

# str = '123456'
# Digits = list(map(int, str))
# print(Digits)

# New = set('123')

# print(New)

# def is_prime(n):
#     if n <= 1: 
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6

#     return True


# print(ord('a'))
# print(chr(97))
# @lru_cache(None)


li = [1,2,3,5,1,2.7]
for i in range(len(li) - 1, -1, -1):
    print(li[i])