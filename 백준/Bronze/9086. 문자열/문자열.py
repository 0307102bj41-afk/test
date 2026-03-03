a = int(input())
for i in range(a):
    list_i = []
    i = input()
    list_i.append(i[0:1:])
    list_i.append(i[len(i):len(i)-2:-1])
    if len(i) == 1:
        print(list_i[0], end='')
        print(list_i[0])
    else:
        print(list_i[0], end='')
        print(list_i[1]) 
