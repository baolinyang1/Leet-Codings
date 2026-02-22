def stan_wins(a: int, b: int) -> bool:
    """
    Returns True if Stan (the first player) wins assuming both play perfectly.
    """

    # Always make sure a >= b
    if a < b:
        a, b = b, a

    stan_turn = True  # True = Stan's turn, False = Ollie's turn

    while True:
        # If smaller number becomes 0, current player cannot move
        if b == 0:
            return not stan_turn

        q = a // b   # how many times b fits inside a
        r = a % b    # remainder after subtracting q*b

        # If q >= 2, current player can subtract 2 or more multiples
        # That means they can force a win immediately.
        if q >= 2:
            return stan_turn

        # If remainder is 0, current player can subtract exactly q*b
        # making the number 0 and winning immediately.
        if r == 0:
            return stan_turn

        # Otherwise q == 1 and r > 0
        # Only one move possible: subtract b once.
        # New state becomes (b, r)
        a, b = b, r

        # Switch turns
        stan_turn = not stan_turn


# -------------------------
# Main program
# -------------------------

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if stan_wins(a, b):
        print("Stan wins")
    else:
        print("Ollie wins")