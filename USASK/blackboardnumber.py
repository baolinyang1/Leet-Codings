# the flow should be: given a number, convert it t base 10, form an array and run through check_prime()

import math

def check_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

T = int(input())
for i in range(T):
    s = input().strip()

    valid = prime_count = 0
    for base in [2, 8, 10, 16]:
        try:
            number = int(s, base)
            valid += 1

            if check_prime(number):
                prime_count += 1

        except ValueError:
            pass
    #greatest common divisor!
    g = math.gcd(prime_count, valid)
    print(f"{prime_count // g}/{valid // g}")