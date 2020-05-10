v=int(input('Enter the number'))
R=0.
while(v>0):
  Rem=v%10
  R=(R*10)+Rem
  v//=10
print(R)