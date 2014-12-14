x = 0

for i in range(1, 101):
    x += i*i

y = 0
for i in range(1, 101):
    y += i

y = y * y

answer = y - x

print(answer)
