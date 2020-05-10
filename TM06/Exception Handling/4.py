z=[1,2,3,4,5,6345,45,-423,76,98]
i=int(input("Enter the index to check the number(0-9): "))
try:
    if(z[i]>=0):
        print("Positive")
    else:
        print("Negative")
except:
    print("Wrong index")
    
