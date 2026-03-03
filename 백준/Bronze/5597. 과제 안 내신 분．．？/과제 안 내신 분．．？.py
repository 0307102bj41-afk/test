list_1 = []
list_2 = []

list_1 = list(range(1,31))

a=28
b=0
for i in range(a):
    b = int(input())
    if b in list_1:
        list_1.remove(b)

print(list_1[0])
print(list_1[1])



