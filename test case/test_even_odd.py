import sys
sys.path.append("code")

from even_odd import check_even_odd

assert check_even_odd(2) == "even"
assert check_even_odd(5) == "odd"
assert check_even_odd(0) == "even"
assert check_even_odd(-4) == "even"
assert check_even_odd(-7) == "odd"

print("All test cases passed!")