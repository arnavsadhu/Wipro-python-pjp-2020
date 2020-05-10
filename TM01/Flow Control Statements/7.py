for v in range(10,100):
  if v>1: 
   for i in range(2, v//2): 
       if (v% i) == 0: 
           break
   else: 
       print(v, "\n") 