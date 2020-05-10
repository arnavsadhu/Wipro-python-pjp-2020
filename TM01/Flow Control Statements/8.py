v=int(input('Enter the number'))
sum=0
while(v!=0):
  num=v%10
  sum+=num
  v//=10
print(sum)