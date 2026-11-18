def even_generator():
    for i in range(2, 11, 2):
        yield i

g = even_generator()

for num in g:
    print(num)
