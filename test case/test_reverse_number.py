import sys
sys.path.append("code")

from reverse_number import reverse_number

assert reverse_number(1234) == 4321
assert reverse_number(567) == 765
assert reverse_number(100) == 1
assert reverse_number(7) == 7
assert reverse_number(0) == 0
assert reverse_number(-123) == -321

print("All test cases passed!")