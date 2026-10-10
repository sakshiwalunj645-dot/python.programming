def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("The number is", check_number(num))