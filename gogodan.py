#week3 구구단 출력하기 

a = 0
while a < 9:
    a = a + 1
    b = 0
    while b < 9:
        b = b +1
        print(a, '*', b, '=', (a*b), " ", end=" ")
    print("\n")
