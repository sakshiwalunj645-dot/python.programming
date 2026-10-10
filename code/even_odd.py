def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("The number is", check_even_odd(num))