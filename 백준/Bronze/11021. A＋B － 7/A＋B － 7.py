# 이건 py파일 따로 만들어서 실행, 쥬피터에선 이거 안됨
import sys
input = sys.stdin.readline # 이렇게 하면 sys를 전부 input으로 평소하던대로 ㄱㄴ

a = int(input())
for i in range(a):
    b, c = map(int, input().split())
    print(f'Case #{i+1}: {b+c}')
    