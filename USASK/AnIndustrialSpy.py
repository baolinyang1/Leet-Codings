# from itertools import permutations
# def isPrime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
    
#     if n % 2 == 0 or n % 3 == 0:
#         return False
    
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i+2) == 0:
#             return False
#         i += 6
#     return True

# def check(numberstr: str) -> int:
#     unique = set()

#     # allow using any subset length (ignore digits)
#     for r in range(1, len(numberstr) + 1):
#         for p in permutations(numberstr, r): # super important, this r is how many digits from the str will be used for permuatation
#             num = int(''.join(p))   # strips leading zeros
#             unique.add(num)
#     #advaced adding!
#     return sum(1 for num in unique if isPrime(num))



# Cases = int(input())
# for i in range(0, Cases):
#     numberstr = input()
#     print(check(numberstr))
    
#better solution:::
def is_prime(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    
    i = 5
    while i * i <= n:
        # Check 5 (6k-1) and 7 (6k+1)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 # Jump to the next potential pair (11 and 13)
    return True

def count_primes_from_digits(s: str) -> int:
    digits = sorted(s)          # sorting helps skip duplicates
    used = [False] * len(digits)
    memo = {}                   # prime memo: num -> True/False
    seen = set()                # numbers already formed (to avoid leading-zero duplicates)

    def dfs(curr: str):
        if curr:
            num = int(curr)     # "011" -> 11 (leading zeros collapse)
            if num not in seen:
                seen.add(num)

        for i in range(len(digits)):
            if used[i]:
                continue
            # skip duplicates at the same recursion depth
            if i > 0 and digits[i] == digits[i-1] and not used[i-1]:
                continue

            used[i] = True
            dfs(curr + digits[i])
            used[i] = False

    dfs("")

    ans = 0
    for num in seen:
        if num not in memo:
            memo[num] = is_prime(num)
        if memo[num]:
            ans += 1
    return ans

# main
c = int(input().strip())
for _ in range(c):
    s = input().strip()
    print(count_primes_from_digits(s))
