a= int(input())
result= 0
list_1 = []

list_1 = list(map(int, input().split()))
list_max = max(list_1)
for i in range(a):
    result += list_1[i]*100/list_max/a

print(result)
