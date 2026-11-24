try:
    file = open("demo.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")
