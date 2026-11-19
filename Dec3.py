def my_decorator(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function is completed")
    return wrapper

@my_decorator
def display():
    print("Python Programming")

display()
