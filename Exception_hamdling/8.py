try:
    student = {
        "name": "Rahul",
        "age": 21
    }

    print(student["marks"])

except KeyError:
    print("Key not found")
