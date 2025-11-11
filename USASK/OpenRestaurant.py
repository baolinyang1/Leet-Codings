def weighted_median(weights):  # weights is 1..K (index 0 unused)
    total = sum(weights[1:])
    half = (total + 1) // 2
    acc = 0
    for i in range(1, len(weights)):
        acc += weights[i]
        if acc >= half:
            return i
    return len(weights) - 1

n, m = map(int, input().split())

row_w = [0] * (n + 1)   # row totals (1-indexed)
col_w = [0] * (m + 1)   # column totals (1-indexed)

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    row_w[i] = sum(row)
    for j, val in enumerate(row, start=1):
        col_w[j] += val

r = weighted_median(row_w)
c = weighted_median(col_w)

cost = sum(row_w[i] * abs(i - r) for i in range(1, n + 1)) + \
       sum(col_w[j] * abs(j - c) for j in range(1, m + 1))

print(cost)
