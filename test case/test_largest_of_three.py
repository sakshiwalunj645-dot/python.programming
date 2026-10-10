import sys
sys.path.append("code")

from largest_of_three import largest_of_three

assert largest_of_three(10, 20, 30) == 30
assert largest_of_three(50, 20, 10) == 50
assert largest_of_three(10, 40, 20) == 40
assert largest_of_three(5, 5, 2) == 5
assert largest_of_three(-1, -5, -3) == -1

print("All test cases passed!")