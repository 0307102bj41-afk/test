a,b = map(int, input().split())
c = int(input())
b_and_c = b+c

if b+c >= 60:
    a += b_and_c//60
    
    b_and_c -= 60*(b_and_c//60)

    if a >= 24:
        a-=24

print(f"{a} {b_and_c}")        
    
    