s=input('Enter string:')
if((s[0]=='x')&(s[-1]=='x')):
    print(s[1:-1])
elif(s[0]=='x'):
    print(s[1:])
elif(s[-1]=='x'):
    print(s[:-1])
else:
    print(s)