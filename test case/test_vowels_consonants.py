import sys
sys.path.append("code")

from vowels_consonants import count_vowels_consonants

assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("Python") == (1, 5)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("xyz") == (0, 3)
assert count_vowels_consonants("hello world") == (3, 7)
assert count_vowels_consonants("123 !") == (0, 0)
assert count_vowels_consonants("") == (0, 0)

print("All test cases passed!")