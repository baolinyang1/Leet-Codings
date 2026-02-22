def reverse_bits(x: int, bits: int) -> int:
    """
    Reverse exactly `bits` bits of x.
    Example: x=0b101 (5), bits=3 -> returns 0b101 (5)
             x=0b110 (6), bits=3 -> returns 0b011 (3)
    """
    r = 0
    for _ in range(bits):
        r = (r << 1) | (x & 1)   # take lowest bit of x and append to r
        x >>= 1                  # shift x right to process next bit
    return r


def build_palindrome(left: int, length: int) -> int:
    """
    Build a binary palindrome of total bit-length `length`
    using `left` as the left half (including the middle bit if length is odd).

    length even:  left = abc..., palindrome = left + reverse(left)
    length odd:   left = abc(middle), palindrome = left + reverse(left without middle)
    """
    if length % 2 == 0:
        # length = 2k
        k = length // 2
        right = reverse_bits(left, k)
        return (left << k) | right
    else:
        # length = 2k - 1, where left has k bits (includes the middle bit)
        k = (length + 1) // 2
        # drop the middle bit before mirroring
        right = reverse_bits(left >> 1, k - 1)
        return (left << (k - 1)) | right


def kth_base2_palindrome(m: int) -> int:
    """
    Return the m-th positive integer whose binary representation is a palindrome.
    m is 1-indexed.
    """
    length = 1
    while True:
        # number of palindromes with this bit length
        # k = ceil(length/2)
        k = (length + 1) // 2
        count = 1 << (k - 1)  # 2^(k-1), because left half must start with 1

        if m > count:
            m -= count
            length += 1
        else:
            # The m-th palindrome is in this length group.
            # m is 1..count, convert to 0-based index:
            idx = m - 1

            # left half is k bits, leading bit must be 1:
            # smallest left = 1000...0 (k bits) = 1<<(k-1)
            left = (1 << (k - 1)) | idx

            return build_palindrome(left, length)


# -------- main --------
M = int(input().strip())
print(kth_base2_palindrome(M))