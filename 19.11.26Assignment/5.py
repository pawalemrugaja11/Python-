# Import reduce function
from functools import reduce

# Create list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Using map() to calculate squares
squares = list(map(lambda x: x * x, numbers))


# Using filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


# Using reduce() to calculate sum
total = reduce(lambda x, y: x + y, numbers)


# Display results
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Sum:", total)
