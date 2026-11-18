def my_generator():
    for i in range(1, 6):
        yield i

g = my_generator()

for value in g:
    print(value)
