#use greedy!!!
FirstLine = input()
SecondLine = input()
ThirdLine = input()
FourthLine = input()

# N, M, K not strictly needed for this approach, but you can parse if you want:
# N, M, K = map(int, FirstLine.split())

Array_Plots = sorted([int(n) for n in SecondLine.split()])
Round_Houses = sorted([int(n) for n in ThirdLine.split()])
Square_Houses = sorted([int(n) for n in FourthLine.split()])

# Build requirements list: plot radius must be STRICTLY greater than req
results = []

# round houses: need p > r
for r in Round_Houses:
    results.append(float(r))

# square houses: need p > s / sqrt(2)
root2 = 2 ** 0.5
for s in Square_Houses:
    results.append(s / root2)

results.sort()

# Greedy match smallest requirement to smallest plot that fits
i = 0  # pointer for plots
j = 0  # pointer for requirements
count = 0
eps = 1e-12  # tiny buffer for float comparisons

while i < len(Array_Plots) and j < len(results):
    if Array_Plots[i] > results[j] + eps:   # strict: cannot touch boundary
        count += 1
        i += 1
        j += 1
    else:
        i += 1

print(count)

### numpy solution:
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