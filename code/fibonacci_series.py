def fibonacci_series(n):
    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci series:", fibonacci_series(n))