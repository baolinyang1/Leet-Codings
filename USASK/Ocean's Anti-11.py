# Key idea here is to use Fibonacci sequence
# let An be the nmber of binary sequences of length with no substring "11"
# split by the last char: strings end with 0, have An-1 strings, or Strings end with 1, then the previous cahr must be 0, so it has An-2 strings
# so An = An-1 + An-2, with A0 = 1(even though the problem says n >= 1, bt for the sake of argument, have to figure out base case), A1 = 2
# Then if you remember the Fibo: but they have F0 = 0, F1 = 1, F2 = 1, F3 = 2
# Ours is just a simple shift! A0 = 1 = F2, A1 = 2 = F3, So An = Fn+2

# Recursion is the key!
MOD = 10**9 + 7

T = int(input())
n_values = [int(input()) for _ in range(T)]

max_n = max(n_values)

# Build Fibonacci numbers up to n+2
F = [0] * (max_n + 3)
F[0], F[1] = 0, 1
for i in range(2, max_n + 3):
    F[i] = (F[i-1] + F[i-2]) % MOD

# For each n, answer is F[n+2]
for n in n_values:
    print(F[n + 2] % MOD)
