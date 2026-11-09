#https://open.kattis.com/problems/names

s = input()
n = len(s)

ans = n // 2

#When adding k letters, those new letters can match the first k original letters. Therefore, we only need to check whether s[k:] is a palindrome.
# because when we add letters to the end, we can use them to match the letters at the beginning.
for added in range(n // 2 + 1):
    changes = added
    left = added
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            changes += 1

        left += 1
        right -= 1

    ans = min(ans, changes)
print(ans)
