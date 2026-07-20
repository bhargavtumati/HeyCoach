#write a generator function to generate fibonacci numbers


def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a  
        a, b = b, a + b

print(fibonacci_gen(10))