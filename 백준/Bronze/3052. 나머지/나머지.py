list_1 =[]

for i in range(1, 11):
    a = int(input())
    list_1.append(a%42)

set_1 = set(list_1) 

print(len(set_1))
