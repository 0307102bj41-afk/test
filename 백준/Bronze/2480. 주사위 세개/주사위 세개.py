a,b,c = map(int, input().split())

if a==b==c:
    print(f'{10000 + 1000*a}')
    
elif (a==b or a==c or b==c) and not(a==b==c):
    if (a==b) and not (c==a):
        print(f'{1000 + 100*a}')
    elif (b==c) and not(a==b):
        print(f'{1000 + 100*b}')
    else:
        print(f'{1000 + 100*c}')

else:
    if a > b and a > c:
        print(f'{a*100}')
    elif b > a and b > c:
        print(f'{b*100}')
    else:
        print(f'{c*100}')