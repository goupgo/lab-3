so = input('Enter number: ')
n = int(so)

def tong(n):
    if n == 1:
        return n
    else:
        return n + tong(n - 1)
    
print('Sum is:', tong(n))