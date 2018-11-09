def isOdd(n):
    if n%2 == 1:
        return True
    else:
        return False
# 输入-1程序结束运行    
while True:
    s = input("Plese enter an Integer:")   
    if not s.isdigit():
        print("Please enter again!")
        continue
    n = eval(s)
    if n == -1:
        print("program is over!")
        break
    if isOdd(n):
        print("{} is odd".format(n))
    else:
        print("{} is even".format(n))
