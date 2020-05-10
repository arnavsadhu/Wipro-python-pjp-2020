def checkPrime(z):
  if(z<=1):
    return False
  for i in range (2,z):
    if (z%i==0):
      return False
  return True

try:
  z=int(input("Enter number to check for prime: "))
  p= checkPrime(z)
except:
  print("Input needs to be of only integer type")
else:
  print("Result: ",p)
