def hamming_distance(x, y):
    if len(x) != len(y):
        raise ValueError("Строки не равны")
    distance = sum(c1 != c2 for c1, c2 in zip(x, y))
    return distance
x = "karolin"
y = "kathrin"
print(f"Расстояние Хэмминга между '{x}' и '{y}' равно: {hamming_distance(x, y)}")