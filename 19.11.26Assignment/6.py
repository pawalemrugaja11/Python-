# Define decorator function
def execution_time(func):

    # Define wrapper function
    def wrapper():

        # Message before execution
        print("Function Started")

        # Call original function
        func()

        # Message after execution
        print("Function Finished")

    return wrapper


# Apply decorator
@execution_time
def factorial():

    # Initialize variables
    num = 5
    fact = 1

    # Calculate factorial
    for i in range(1, num + 1):
        fact = fact * i

    # Display factorial
    print("Factorial:", fact)


# Call factorial function
factorial()
