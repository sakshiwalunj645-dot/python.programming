def is_palindrome(num):
    if num < 0:
        return False

    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return original == reverse


if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if is_palindrome(num):
        print("Palindrome number")
    else:
        print("Not a palindrome number")