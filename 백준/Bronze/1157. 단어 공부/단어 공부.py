counts = [0] * 26
word = input()
word = word.upper()
for i in range(len(word)):
    counts[ord(word[i])-65] += 1
    maxvalue = max(counts)

if counts.count(maxvalue) > 1 :
    print('?')
else:
    print(chr(counts.index(maxvalue)+65))