def odd_generator():
    for i in range(1, 10, 2):
        yield i

for num in odd_generator():
    print(num)
