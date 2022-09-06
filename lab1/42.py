n = int(input())
# n = 8
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s = s + i
print(s)
