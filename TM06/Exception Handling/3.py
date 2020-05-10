z=input("Enter the name of the file to be opened: ")
f1=None
try:
  f1=open(z)
  for line in f1:
    l=line.title()
    print(l)
  f1.close()
except:
  print("File does not exist.")

