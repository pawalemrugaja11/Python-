def square_generator():
    for i in range(1, 6):
        yield i * i

for num in square_generator():
    print(num)
