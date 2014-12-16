import math

for i in range(1,1000):
    for j in range(i, 1000):
        k = i*i + j*j
        l = math.sqrt(k)
        m = int(l)
        if m == l:
            if (i + j + m) == 1000:
                print("{} : {} : {}".format(i, j, m))
                print(i*j*m)
                break
