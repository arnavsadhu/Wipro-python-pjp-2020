def printEven(x):
    l=[]
    for i in x:
        if i%2==0:
            l.append(i)
    print(l)
a=[1,2,3,4,5,6,7,8,9,0,456,65,428]
printEven(a)