'''
Key insight (this is the whole trick)
With adjacent swaps, the minimum number of swaps needed to sort is exactly:
The number of inversions
An inversion is a pair (i, j) such that:
i < j
but a[i] > a[j]
Which inversions matter here?
Since valid order is 0 < 1 < 2, the bad pairs are:
1 before 0
2 before 0
2 before 1
Each such pair must be swapped at least once, and each swap fixes exactly one inversion.

So:
answer =
(# of (1 before 0))
+ (# of (2 before 0))
+ (# of (2 before 1))

Scan left to right, keep counters:
c0 = how many 0s seen so far
c1 = how many 1s seen so far
c2 = how many 2s seen so far
When you see: gotta inversions!
0 → it is bad with all previous 1s and 2s
1 → it is bad with all previous 2s
2 → no problem (2 is largest)
'''

s = input().strip()

c0 = c1 = c2 = 0
ans = 0

for ch in s:
    if ch == 0:
        ans += c1 + c2
        c0 += 1
    elif ch == '1':
        ans += c2
        c1 += 1
    else:
        c2 += 1

print(ans)