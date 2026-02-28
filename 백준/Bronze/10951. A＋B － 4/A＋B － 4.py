# 이건 py파일 따로 만들어서 실행, 쥬피터에선 이거 안됨
import sys
input = sys.stdin.readline # 이렇게 하면 sys를 전부 input으로 평소하던대로 ㄱㄴ

while True:
    try:
       a, b = map(int, input().split())
       print(f'{a+b}')
    except:
        break

    


