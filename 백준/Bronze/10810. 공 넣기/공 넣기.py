list_1 = []
a, b = map(int, input().split())

for i in range(a):
    list_1.append(0)

for i in range(b):
    c,d,e = map(int, input().split())
    for j in range(d-c+1):
        list_1[c+j-1] = e

for i in range(len(list_1)):
    print(list_1[i], end=' ')

        
