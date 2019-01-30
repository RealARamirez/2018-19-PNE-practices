Sum = []
n = 150
a, b = 0, 1
c = 0
while a < n:
    c = c + a
    a, b = b, a+b
print(c)

