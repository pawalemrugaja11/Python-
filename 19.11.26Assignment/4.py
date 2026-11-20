# Function with default argument
def calculate_salary(basic_salary, bonus=2000):

    # Calculate total salary
    total_salary = basic_salary + bonus

    # Display salary
    print("Total Salary:", total_salary)


# Positional Arguments
print("Employee 1 Salary:")
calculate_salary(30000, 2000)


# Keyword Arguments
print("Employee 2 Salary:")
calculate_salary(basic_salary=30000, bonus=5000)


# Default Arguments
print("Employee 3 Salary:")
calculate_salary(25000)
