#1 숫자 입력
#2 손익분기점 구하기
#2-1 a+b == c*x되는값 구하기
#3 x값 출력 없으면 -1 출력
a,b,c = map(int,input().split())
x=0

if  b >= c:
    print(-1)
else:
    while True:
        if a >= (c-b)*x:
            x += 1
        else:
            print(x)
            break