a, b = map(int, input().split())

list_1 = list(map(int, input().split()))

list_2 = []

for i in range(a):
    if list_1[i]<b:
        list_2.append(list_1[i])

for i in range(len(list_2)):
    print(list_2[i], end=' ')


