n = int(input())  # Гараас тоо авлаа
# n = 10
s = 1
for i in range(1, n+1, 1):
    if(n % i == 0):
        s = s * i
print(s)
