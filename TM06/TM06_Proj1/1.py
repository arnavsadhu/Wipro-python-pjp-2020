name = "Purchase-1.txt" #input("Enter file name: ")
try:
    f1 = open(name)
except:
    print("Error -- File does not exist")
else:
    dis =0
    count=0
    sum=0
    free =0
    final =0
    while(True):
        line = f1.readline()
        if not line:
            break
        if not line.isspace():
            flag=0
            list1 = line.split()
            if (list1[1]=='0' or list1[1]=='Free'):
                free +=1
                flag=1
            if list1[0]=="Discount":
                dis = int(list1[1])
                flag=1
            if (flag==0):
                count+=1
                sum += float(list1[1])
           
    final=sum-dis
    print("No. of item Purchased:",count)
    print("No. of free items:",free)
    print("Amount to pay:",sum)
    print("Discount Given:",dis)
    print("Final amount paid:",final)