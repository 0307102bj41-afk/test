a = int(input())
b = input().split()

c = []
for i in range(a):
    c.append(int(b[i]))

d = int(input())
e = c.count(d)
print(e)
