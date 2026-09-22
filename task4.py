"""Task 4: Calculate the factorial of a nonnegative integer."""

number = int(input("Enter a nonnegative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1
    for value in range(2, number + 1):
        factorial *= value

    print(f"{number}! = {factorial}")
