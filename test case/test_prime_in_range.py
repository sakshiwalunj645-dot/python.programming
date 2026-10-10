import sys
sys.path.append("code")

from primes_in_range import prime_in_range

assert prime_in_range(1, 10) == [2, 3, 5, 7]
assert prime_in_range(10, 20) == [11, 13, 17, 19]
assert prime_in_range(2, 5) == [2, 3, 5]
assert prime_in_range(20, 30) == [23, 29]
assert prime_in_range(1, 1) == []
assert prime_in_range(14, 16) == []

print("All test cases passed!")