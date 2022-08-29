n = 8134
s = 1
while(n > 0):
    a = n % 10
    s = s * a
    n = n // 10
print(s)
