import sys
sys.path.append("code")

from factorial import factorial

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(3) == 6
assert factorial(-2) == "undefined"

print("All test cases passed!")