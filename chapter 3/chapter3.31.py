def product_array(a):
    n = len(a)
    p = [1] * n

    left_product = 1
    for i in range(n):
        p[i] = left_product
        left_product *= a[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        p[i] *= right_product
        right_product *= a[i]

    return p

a = [1, 2, 3]
p = product_array(a)
print(p)