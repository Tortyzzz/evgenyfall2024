def scalar_product(a, b):
    return sum(a[i] * b[i] for i in range(3))

def vector_product(a, b):
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

def scalar_mixed_product(a, b, c):
    return scalar_product(a, vector_product(b, c))

def vector_mixed_product(a, b, c):
    return vector_product(a, vector_product(b, c))

a = [0, 4, -4]
b = [9, 2, 1]
c = [2, -4, -3]

print("Скалярное произведение:", scalar_product(a, b))
print("Векторное произведение:", vector_product(a, b))
print("Скалярное смешанное произведение:", scalar_mixed_product(a, b, c))
print("Векторное смешанное произведение:", vector_mixed_product(a, b, c))