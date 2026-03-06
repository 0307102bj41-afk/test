a = str(input())

b = 0

for i in range(len(a)):
    if a[i] == a[len(a)-i-1]:
        b += 1
    else:
        b -= 10000

if b < 1 :
    print(0)
else:
    print(1)

