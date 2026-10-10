import sys
sys.path.append("code")

from palindrome_string import is_palindrome

assert is_palindrome("madam") == True
assert is_palindrome("level") == True
assert is_palindrome("naman") == True
assert is_palindrome("hello") == False
assert is_palindrome("Python") == False
assert is_palindrome("A") == True
assert is_palindrome("") == True

print("All test cases passed!")