import sys
sys.path.append("code")

from sum_of_digits import sum_of_digits

assert sum_of_digits(1234) == 10
assert sum_of_digits(567) == 18
assert sum_of_digits(100) == 1
assert sum_of_digits(9) == 9
assert sum_of_digits(0) == 0
assert sum_of_digits(-123) == 6

print("All test cases passed!")