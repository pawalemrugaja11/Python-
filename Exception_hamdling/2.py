try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))

    print("Result =", a / b)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")
