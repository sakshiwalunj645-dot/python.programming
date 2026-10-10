import sys
sys.path.append("code")

from char_frequency import char_frequency

assert char_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}

assert char_frequency("aabbc") == {
    "a": 2, "b": 2, "c": 1
}

assert char_frequency("aaa") == {"a": 3}

assert char_frequency("Python") == {
    "P": 1, "y": 1, "t": 1,
    "h": 1, "o": 1, "n": 1
}

assert char_frequency("") == {}

print("All test cases passed!")