def tbedge(n):
     print('+ - - - - ' * n + '+')
def lredge(n):
     print('|         ' * n + '|')
def matts(n):
    for i in range(5*n+1):
        if i%5==0:
            tbedge(5)
        else:
            lredge(5)
matts(5)
            
                

          
