import re
inp = input('Please input two integers: ')
a, b = [int(i) for i in re.findall(r'\d+', inp)]
 
def gys(m, n):
    if m == 1 or m == n:
        return m    
    for i in range(min(m, n), 0, -1):
        if m%i == 0 and n%i == 0:
            return i
 
g = gys(a, b)           
print('最大公约数: ', g)
print('最小公倍数: ', a*b//g)
