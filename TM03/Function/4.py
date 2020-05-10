def countUpperLower(s):
    U,L=0,0
    for i in range(len(s)):
        if(ord(s[i])<=122 and ord(s[i])>=97):
            U+=1
        elif(ord(s[i])<=90 and ord(s[i])>=65):
            L+=1
    print("Upper Count: ", U,"\nLower Count: ",L);

z=input("Input a string:")
countUpperLower(z)     