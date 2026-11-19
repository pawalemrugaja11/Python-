def check_number(func):
    def wrapper(n):
        if n > 0:
            print("Positive Number")
        elif n < 0:
            print("Negative Number")
        else:
            print("Zero")
        func(n)
    return wrapper

@check_number
def display(n):
    print("Number is:", n)

display(10)
