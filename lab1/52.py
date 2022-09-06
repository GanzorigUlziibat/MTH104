n = int(input())
# n = 1234
s = 1
while(n > 0):
    so = n % 10  # suuliin oron
    s = s * so  # orongiin urjveruud
    n = n // 10  # suuliin orong taslaj baina
print(s)
