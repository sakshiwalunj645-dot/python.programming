import sys

sys.path.append("code")

from remove_duplicates import remove_duplicates

assert remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
assert remove_duplicates([5, 5, 5]) == [5]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]

print("All test cases passed")