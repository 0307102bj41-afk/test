a = input()

for i in range(26):
    if chr(i+97) in a:
        print(a.find(chr(i+97)), end=" ")
    else:
        print(-1, end=" ")
