# Import date and timedelta
from datetime import date, timedelta


# Generator function
def generate_dates():

    # Get today's date
    today = date.today()

    # Generate dates for next 7 days
    for i in range(7):

        # Generate one date at a time
        yield today + timedelta(days=i)


# Display generated dates
print("Next 7 Days:")

for d in generate_dates():
    print(d)
