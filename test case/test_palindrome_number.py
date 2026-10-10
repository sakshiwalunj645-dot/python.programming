import sys
sys.path.append("code")

from palindrome_number import is_palindrome

assert is_palindrome(121) == True
assert is_palindrome(12321) == True
assert is_palindrome(123) == False
assert is_palindrome(10) == False
assert is_palindrome(0) == True
assert is_palindrome(-121) == False

print("All test cases passed!")