# Read input:
# N = number of guests
# H = number of candles each guest brings
# C = maximum total effort Minka can spend
N, H, C = map(int, input().split())

# prefix[i][t] will store:
# minimum effort to blow exactly t candles from guest i
prefix = []

# Process each guest
for _ in range(N):
    # Read the H candle efforts for this guest
    arr = list(map(int, input().split()))
    
    # Sort so cheapest candles come first
    arr.sort()
    
    # pre[t] = minimum cost to blow t candles from this guest
    # size H+1 because t can be from 0 to H
    pre = [0] * (H + 1)
    
    s = 0  # running sum
    for i in range(H):
        s += arr[i]          # add next cheapest candle
        pre[i + 1] = s       # cost of blowing (i+1) candles
    
    # Save this guest's prefix cost array
    prefix.append(pre)

# best will store the maximum candles we can blow
best = 0

# Try every possible base number x
# meaning every guest blows either x or x+1 candles
for x in range(H + 1):

    # Compute cost if EVERY guest blows exactly x candles
    base_cost = 0
    for i in range(N):
        base_cost += prefix[i][x]

    # If even this base cost exceeds capacity, skip this x
    if base_cost > C:
        continue

    # Total candles blown so far
    total = N * x

    # Try upgrading some guests from x to x+1
    # (only possible if x < H)
    if x < H:
        deltas = []

        # Compute extra cost for upgrading each guest
        # extra cost = cost(x+1) - cost(x)
        for i in range(N):
            extra = prefix[i][x + 1] - prefix[i][x]
            deltas.append(extra)

        # Sort upgrade costs (greedy: take cheapest upgrades first)
        deltas.sort()

        cur = base_cost  # current total effort used

        # Try taking upgrades while within budget
        for d in deltas:
            if cur + d <= C:
                cur += d
                total += 1   # one more candle blown
            else:
                break

    # Update best answer
    best = max(best, total)

# Output the maximum candles Minka can blow
print(best)