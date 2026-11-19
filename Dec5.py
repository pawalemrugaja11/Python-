def square_decorator(func):
    def wrapper(n):
        result = func(n)
        return result * result
    return wrapper

@square_decorator
def number(n):
    return n

print(number(5))
