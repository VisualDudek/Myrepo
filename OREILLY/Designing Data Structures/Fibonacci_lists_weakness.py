
# Python list Primary Weakness
# Avoid functions that return list objects whose values are simply iterated -> Consider generator


def fibonacci_list(n):
    a = b = 1
    result = [a,b]
    while n > 2:
        n -= 1
        a,b = b,a+b
        result.append(b)
    return result

print(fibonacci_list(10))


# Generator avoids constructing lists
def fibonacci_generator(n):
    a = b = 1
    yield a
    yield b
    while n > 2:
        n -= 1
        a,b = b,a+b
        yield b

print(list(fibonacci_generator(10)))
