#https://open.kattis.com/problems/knitpicking
#Find the maximum number of socks you can draw without forming a pair, then answer is that number + 1.

N = int(input())
socks = {}
for _ in range(N):
    sock_type, fit, number = input().split()
    number = int(number)
    if sock_type not in socks:
        socks[sock_type] = {
            "left": 0,
            "right": 0,
            "any": 0
        }
    socks[sock_type][fit] = number

safe_total = 0
pair_possible = False

for counts in socks.values():
    left = counts["left"]
    right = counts["right"]
    any_count = counts["any"]
    # maximum number we can take from this type
    # while still avoiding a pair
    safe_total += max(left, right, min(any_count, 1))
    # Check whether this type can ever make a pair
    if left > 0 and right > 0:
        pair_possible = True
    if any_count >= 2:
        pair_possible = True
    if any_count > 0 and (left > 0 or right > 0):
        pair_possible = True

if not pair_possible:
    print("impossible")
else:
    print(safe_total + 1)