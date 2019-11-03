def Bb(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)


a = int(input("请输入数字："))
Bb(a)
