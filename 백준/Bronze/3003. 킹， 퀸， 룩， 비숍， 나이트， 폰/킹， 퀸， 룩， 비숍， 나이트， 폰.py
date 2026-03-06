a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))

for i in range(len(a)):
    a[i] = int(a[i]) - b[i]
for i in range(len(a)):
    print(a[i], end=' ')