# Function to analyze numbers
def analyze_numbers(numbers):

    # Find maximum value
    maximum = max(numbers)

    # Find minimum value
    minimum = min(numbers)

    # Calculate sum
    total = sum(numbers)

    # Calculate average
    average = total / len(numbers)

    # Display results
    print("Maximum =", maximum)
    print("Minimum =", minimum)
    print("Sum =", total)
    print("Average =", average)


# Main program
numbers = [10, 20, 30, 40]

# Function calling
analyze_numbers(numbers)
