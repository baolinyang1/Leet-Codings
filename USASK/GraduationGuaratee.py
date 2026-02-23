def main():
    # Read input
    n, k = map(int, input().split())
    ps = list(map(float, input().split()))

    # Sort probabilities in descending order
    ps.sort(reverse=True)

    # dp represents probabilities of scores
    # For m answered questions, score range is [-m, m]
    # Start with m = 0 → score = 0 with probability 1
    dp = [1.0]
    offset = 0  # score = index - offset

    # If k <= 0, passing is guaranteed
    best = 1.0 if k <= 0 else 0.0

    for p in ps:
        q = 1.0 - p

        # Expand dp for one more question
        new_dp = [0.0] * (len(dp) + 2)

        for i in range(len(dp)):
            val = dp[i]
            if val > 0:
                # score - 1
                new_dp[i] += val * q
                # score + 1
                new_dp[i + 2] += val * p

        dp = new_dp
        offset += 1  # we added one more question

        # Compute probability that score >= k
        # score >= k  <=>  index >= offset + k
        idx = offset + k

        if idx <= 0:
            pass_prob = 1.0
        elif idx >= len(dp):
            pass_prob = 0.0
        else:
            pass_prob = sum(dp[idx:])

        best = max(best, pass_prob)

    print(f"{best:.10f}")


main()