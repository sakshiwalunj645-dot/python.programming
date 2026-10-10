import sys
sys.path.append("code")

from prime_number import is_prime

assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(7) == True
assert is_prime(1) == False
assert is_prime(0) == False
assert is_prime(-5) == False
assert is_prime(13) == True

print("All test cases passed!")