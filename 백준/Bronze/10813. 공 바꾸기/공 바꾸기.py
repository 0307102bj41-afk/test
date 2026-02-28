list_1 = []

N, M = map(int, input().split())

for i in range(N):
    list_1.append(i+1)

for j in range(M):
    a, b = map(int, input().split())
    temp = list_1[a-1]
    list_1[a-1] = list_1[b-1]
    list_1[b-1] = temp

print(*list_1)