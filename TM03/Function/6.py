def Prime(n):
    if (n <= 1): 
        return False
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True
z=int(input('Enter number to check for prime:'))
if Prime(z): 
    print ("True") 
else: 
    print ("false") 