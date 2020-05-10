s=input('Enter string:')
n=int(input('Enter n:'))
it=s[-n:]
z=''
for x in range(n):
    z+=it
print(z)