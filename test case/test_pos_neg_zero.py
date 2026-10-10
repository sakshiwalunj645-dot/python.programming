import sys
sys.path.append("code")

from pos_neg_zero import check_number

assert check_number(10) == "positive"
assert check_number(-5) == "negative"
assert check_number(0) == "zero"
assert check_number(100) == "positive"
assert check_number(-20) == "negative"

print("All test cases passed!")