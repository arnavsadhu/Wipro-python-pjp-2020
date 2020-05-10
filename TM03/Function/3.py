def fact(x):
    s=1
    for i in range(1,x+1):
        s*=i
    return s

li=int(input("Input number: "))
print(fact(li))