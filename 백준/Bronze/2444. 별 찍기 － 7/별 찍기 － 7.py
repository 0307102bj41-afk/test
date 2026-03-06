a = int(input())
b = []

for i in range(a):
    print((" "*(a-i-1)), end='')
    print('*'*(2*(i)+1))
for i in range(1, a):
    print(" "*(i), end = '')
    print('*'*(2*(a-i)-1))

