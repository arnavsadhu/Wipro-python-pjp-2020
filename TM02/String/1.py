str="My name is Bjourne Sas."
upper, lower = 0, 0
for i in range(len(str)): 
    if str[i] >= 'A' and str[i] <= 'Z': 
        upper += 1
    elif str[i] >= 'a' and str[i] <= 'z': 
        lower += 1
print('Upper case letters:', upper) 
print('Lower case letters:', lower) 