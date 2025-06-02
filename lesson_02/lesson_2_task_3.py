def square(n):
    import math
    nn = math.ceil(n)
    result = nn*nn
    return result


n = int(input("Введите сторону квадрата "))
print(square(n))
