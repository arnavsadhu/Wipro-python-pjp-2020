v=int(input('enter the number to check for prime:'))
if v>1: 
   for i in range(2, v//2): 
       if (v% i) == 0: 
           print(v, "is not a prime number") 
           break
   else: 
       print(v, "is a prime number")
else: 
   print(v, "is not a prime number") 