v=int(input('Enter the number'))
R=0
v1=v
while(v>0):
  Rem=v%10
  R=(R*10)+Rem
  v//=10
if(v1==R):
  print('Pallindrome')
else:
  print('not a pallindrome')