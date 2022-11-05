#This Program is to give the Result to find how many Conbinations of a given set Values

def fact(n):
    if n == 1:
        return n
    else:
        return n* fact(n-1)
        
        
def com(n,r):
    if r == 1:
        return fact(n)
    else:
        return (fact(n)//(fact(r)*fact(n-r)))



n, r = list(map(int, input().split(' ')))

if r <= 0:
    print('Entered Value not Valid! ')
elif n < r:
    print("N should be greater than R.")
else:
    print(com(n,r))
