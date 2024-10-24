for i in range(1,9999999):
    s = 1
    s1 = 0
    for j in range(1,i):
       s *= j
    for j in str(s):
        s1 += int(j)
    if s % s1 != 0:
        print(i)
        break