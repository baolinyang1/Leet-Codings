import numpy as np
FirstLine = input()
SecondLine = input()
ThirdLine = input()
FourthLine = input()

Array_Plots = np.sort(np.fromstring(SecondLine, sep=" ", dtype=np.int64))
Round_Houses = np.fromstring(ThirdLine, sep = " ", dtype=np.float64)
Square_Houses = np.fromstring(FourthLine, sep=" ", dtype=np.float64)

root2 = np.sqrt(2.0)

results = np.sort(np.concatenate([Round_Houses, Square_Houses / root2]))

i = 0
j = 0
count = 0
eps = 1e-12

while i < Array_Plots.size and j < results.size:
    if Array_Plots[i] > results[j] + eps:
        count += 1
        j += 1
        i += 1
    else:
        i += 1
print(count)