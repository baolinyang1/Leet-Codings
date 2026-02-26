def can_split_with_max_len(N, L, req, X):
    """
    Return True if we can partition wagons 1..N into <= L consecutive segments
    such that every segment sent to Luxembourg has length <= X.
    req is the sorted list of required wagon indices.
    """
    W = len(req)
    idx = 0          # index into req[]
    pos = 1          # next wagon position not yet assigned to any segment
    segments = 0     # total segments used (Lux + NL)

    while pos <= N:
        # If all required wagons are already covered, the rest can be 1 NL segment.
        if idx >= W:
            segments += 1
            break

        next_req = req[idx]

        # If we cannot reach the next required wagon within a Lux segment of length X
        # starting at pos, then pos..next_req-1 contains no required wagons -> NL segment.
        if next_req - pos + 1 > X:
            segments += 1
            pos = next_req  # jump to where the next required wagon is
        else:
            # Create a Luxembourg segment starting at pos with maximum length X
            segments += 1
            end = min(N, pos + X - 1)

            # Mark all required wagons covered by this Luxembourg segment
            while idx < W and req[idx] <= end:
                idx += 1

            pos = end + 1  # next uncovered wagon

        # Early stop if we already exceed the allowed number of segments
        if segments > L:
            return False

    return segments <= L


def solve_one_case(N, W, L, req):
    # Binary search the minimum possible maximum Luxembourg-train length.
    lo, hi = 1, N
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split_with_max_len(N, L, req, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    T = int(input().strip())
    for _ in range(T):
        N, W, L = map(int, input().split())
        req = list(map(int, input().split())) if W > 0 else []
        print(solve_one_case(N, W, L, req))


if __name__ == "__main__":
    main()