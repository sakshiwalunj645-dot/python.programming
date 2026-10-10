import sys
sys.path.append("code")

from second_largest_number import second_largest_number

assert second_largest_number([10, 20, 30, 40]) == 30
assert second_largest_number([5, 1, 9, 3]) == 5
assert second_largest_number([10, 10, 8, 7]) == 8
assert second_largest_number([-1, -5, -3]) == -3
assert second_largest_number([1, 1, 1]) == None
assert second_largest_number([5]) == None

print("All test cases passed!")