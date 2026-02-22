import math


def max_sum_from(v: int, steps: int) -> int:
    """
    Compute the maximum zig-zag sum achievable in `steps` moves
    starting from current letter value `v` (where v is 1..26).

    Strategy for maximizing:
    - First jump: go to whichever end ('a' or 'z') is farther.
    - After reaching an end, keep bouncing between 'a' and 'z'.
      Each bounce adds 25 (maximum possible difference).
    """

    # If no steps left, no additional sum can be added
    if steps == 0:
        return 0

    # Largest possible first jump:
    # distance to 'a'  = v - 1
    # distance to 'z'  = 26 - v
    first = max(v - 1, 26 - v)

    # After first move, every remaining move can contribute 25
    # by bouncing between the two ends.
    return first + 25 * (steps - 1)


def solve(k: int) -> str:
    """
    Construct the shortest lexicographically smallest lowercase string
    whose zig-zag value equals exactly k.

    Zig-zag value is defined as:
        |x1 - x2| + |x2 - x3| + ... + |x(n-1) - xn|
    where letters map as a=1, b=2, ..., z=26.
    """

    # -----------------------------------------
    # Step 1: Determine minimum number of steps
    # -----------------------------------------

    # Each step contributes at most 25.
    # So we need at least ceil(k / 25) steps.
    m = (k + 24) // 25   # ceiling division trick

    # Number of letters = steps + 1
    n = m + 1

    # -----------------------------------------
    # Step 2: Initialize construction
    # -----------------------------------------

    # Start with 'a' (value 1) for lexicographically smallest result
    vals = [1]

    # Current letter value
    v = 1

    # Remaining zig-zag sum to achieve
    remaining_sum = k

    # Remaining steps we can still use
    remaining_steps = m

    # -----------------------------------------
    # Step 3: Build the string greedily
    # -----------------------------------------

    # We already have first letter, so we need n-1 more letters
    for _ in range(n - 1):

        # Try every possible next letter from smallest to largest
        for u in range(1, 27):

            # Contribution if we move from current letter v to u
            d = abs(u - v)

            # Remaining sum after choosing this letter
            s2 = remaining_sum - d

            # Remaining steps after choosing this letter
            steps2 = remaining_steps - 1

            # If this choice already exceeds required sum, skip
            if s2 < 0:
                continue

            # -----------------------------
            # Case 1: This is the last step
            # -----------------------------
            if steps2 == 0:

                # We must finish exactly at zero remaining sum
                if s2 == 0:
                    vals.append(u)
                    v = u
                    remaining_sum = s2
                    remaining_steps = steps2
                    break

            # -----------------------------
            # Case 2: More steps remain
            # -----------------------------
            else:
                # Check if it's still possible to finish.
                # Remaining required sum must be <= maximum possible
                # achievable from this new position.
                if s2 <= max_sum_from(u, steps2):
                    vals.append(u)
                    v = u
                    remaining_sum = s2
                    remaining_steps = steps2
                    break

    # -----------------------------------------
    # Step 4: Convert numeric values to letters
    # -----------------------------------------

    # Convert 1→'a', 2→'b', ..., 26→'z'
    # ord('a') gives ASCII value of 'a'
    # chr(number) converts ASCII value back to character
    return "".join(chr(ord('a') + x - 1) for x in vals)


# -----------------------------------------
# Main execution
# -----------------------------------------

# Read integer k
k = int(input().strip())

# Print the constructed string
print(solve(k))