def generator(n):
    for i in range(n):
        yield n


generator0 = generator(10)

for i in generator0:
    print(i)

def simple_generator_function():
    yield 1
    yield 2
    yield 3


gene0 = simple_generator_function()
print(next(gene0))
print(next(gene0))
print(next(gene0))
