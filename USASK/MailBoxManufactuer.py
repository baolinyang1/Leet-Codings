from functools import lru_cache


@lru_cache(None)
def f(k: int, l: int, r: int) -> int:
    """
    f(k, l, r) =
    Minimum crackers needed (worst case)
    to determine T when:
        - k mailboxes left
        - T is between l and r (inclusive)
        - we already know l is safe
    """

    # BASE CASE 1:
    # If l == r, we already know T.
    if l >= r:
        return 0

    # BASE CASE 2:
    # Only one mailbox left.
    # Must test sequentially from l+1 up to r.
    if k == 1:
        n = r - l
        # Sum of (l+1) + (l+2) + ... + r
        return (l + 1 + r) * n // 2

    best = float('inf')

    # Try every possible test value x
    for x in range(l + 1, r + 1):

        # Cost of using x crackers right now
        cost_now = x

        # If mailbox explodes → T < x
        cost_if_break = f(k - 1, l, x - 1)

        # If mailbox survives → T >= x
        cost_if_safe = f(k, x, r)

        # Worst case branch
        worst_future = max(cost_if_break, cost_if_safe)

        total_cost = cost_now + worst_future

        best = min(best, total_cost)

    return best


def main():
    # Read number of test cases
    data = input().strip().split()
    n = int(data[0])

    for _ in range(n):
        # Read k and m for each test
        data = input().strip().split()
        k = int(data[0])
        m = int(data[1])

        print(f(k, 0, m))


if __name__ == "__main__":
    main()
