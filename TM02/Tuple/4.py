tup=(1,2,3,4,5,55,3324,243,243,324,432,432234,346,345,12,4,31,434,56,36,4)
p=int(input('Enter the element to search: '))
x=0
for z in tup:
    x+=1
    if(z==p):
        print('Index:',x)
